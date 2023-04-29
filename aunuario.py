import asyncio,time,yarl,sys,os,http,user_agent,pathlib,random,urllib,logging
from bs4 import BeautifulSoup
from io import (
FileIO,
BufferedReader)
from aiohttp import (
ClientSession,
BaseConnector,
TCPConnector,
CookieJar,
ClientConnectionError
,ServerDisconnectedError,
FormData)
from aiohttp_socks import *
from typing import *

import json as jsn



LOGGER = logging.getLogger(__name__)



class FileReaders(BufferedReader):
    def __init__(self, filename, progressfunc: Callable = None,args:Tuple=None, loop: asyncio.AbstractEventLoop = None):
        f = FileIO(filename,"rb")
        self.progressfunc = progressfunc
        super().__init__(raw=f)
        self.args = args
        self.length = pathlib.Path(filename).stat().st_size
        self.loop: asyncio.AbstractEventLoop = loop
        self.time_start = time.time()

    def read(self, size=None):
        try:
           if not self.progressfunc is None:
            self.loop.run_in_executor(None,self.progressfunc,self.tell(),self.length,self.time_start,self.args,self.loop)
        except Exception as ex:
            print(ex)
        return super(FileReaders, self).read(size)


class LoginException(Exception):
    def __init__(self, message: object):
        self.message = message
        if message is None:
            self.message = "Error al intentar Loguearse"
        super().__init__(self.message)
    def __str__(self) -> str:
        return str(self.message)

class AnuarioClient:
    def __init__(self,
        username: str = "ghost_simon", 
        password: str = "rockstar193@a",
        proxy: str = None,
        loop: asyncio.AbstractEventLoop = None) -> None:

        self.username: str = username
        self.password: str = password
        self.host: yarl.URL = "https://anuarioeco.uo.edu.cu/"
        self.info_proxy:str = proxy
        self.connector_session: BaseConnector = None
        self.session: ClientSession = None
        self.loop: asyncio.AbstractEventLoop = loop
        self.csrfToken: str = None
        if self.loop is None:
            LOGGER.warning("The loop is None")
            return

    @staticmethod
    def created_link(json: Dict) -> yarl.URL:
        return yarl.URL(json['url'])

    async def _create_session(self) -> NoReturn:
        if self.info_proxy is None:
            self.connector_session: BaseConnector = TCPConnector(ssl=False)
        else:
            self.connector_session: BaseConnector = ProxyConnector(ssl=False).from_url(self.info_proxy)
        self.session = ClientSession(
        connector=self.connector_session,
        headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"},
        cookie_jar=CookieJar(unsafe=True,quote_cookie=True)    
        )

    async def verify_login(self) -> bool:
        try:
         async with self.session.get(self.host+"index.php/aeco/user/profile") as reqt:
            print(reqt.url)
            print(self.host+"index.php/aeco/user/profile")
            if str(reqt.url) == str(self.host + "index.php/aeco/user/profile"):
                return True
            else:
                return False
        except (ServerDisconnectedError,ClientConnectionError,Exception):
            await self._create_session() 
            return await self.login_method()

    async def login_method(self):
        prepare_data = FormData()
        prepare_data.add_field("username",self.username)    
        prepare_data.add_field("password",self.password) 
        prepare_data.add_field("source","")
        prepare_data.add_field("remember","1")
        async with self.session.get(self.host+"index.php/aeco/login") as reqt:
            html = await reqt.text()
        soup = BeautifulSoup(markup=html,features="html.parser")
        self.csrfToken = soup.find("input",attrs={"name":"csrfToken"})['value']
        prepare_data.add_field("csrfToken",self.csrfToken)
        print(prepare_data._fields)
        async with self.session.post(self.host+"index.php/aeco/login/signIn",data=prepare_data) as postreq:
            print(postreq.url)
        vl = await self.verify_login()
        if vl:
            return vl
        else:
            raise LoginException("No se pudo loguear")

    async def Upload_File(self,file: pathlib.Path | str,progressfunc: Callable = None, progressargs: Tuple = None, loop: asyncio.AbstractEventLoop = None) -> yarl.URL | bool:
        if loop is None:
            loop = asyncio.get_running_loop()
        prepare_upload_data = FormData()
        prepare_upload_data.add_field("fileStage","2")
        prepare_upload_data.add_field("name[es_ES]",pathlib.Path(file).name)
        prepare_upload_data.add_field("name[en_US]",pathlib.Path(file).name)
        prepare_upload_data.add_field("file",FileReaders(str(file),progressfunc=progressfunc,args=progressargs,loop=loop))
        submissions_id = random.randint(5000,10000) #Hace falta revisar tallas de submission gay ese pero to ta bien
        async with self.session.post(
            self.host + f"index.php/aeco/api/v1/submissions/5368/files",
            data=prepare_upload_data,
            headers = {"X-Csrf-token":self.csrfToken}
        ) as repost:
         try:
          json = await repost.json()
          print(json)
         except:
            json = jsn.loads(await repost.text())
        if "_href" in json:
            return self.created_link(json)
        else:
            return False

