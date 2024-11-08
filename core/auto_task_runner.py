import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

class AutoTaskRunner:
    def __new__(self):
        global auto_task_runner
        
        if auto_task_runner is None:
            auto_task_runner = super().__new__(AutoTaskRunner)
            
        return auto_task_runner
        
    def __init__(self):
        super().__init__()
        chromedriver_autoinstaller.install()
        # Check if the current version of chromedriver exists
        # and if it doesn't exist, download it automatically,
        # then add chromedriver to path               

        self._options = ChromeOptions()
        self._options.add_argument('--disable-infobars')
        self._service = ChromeService('chromedriver.exe')
        self._driver = webdriver.Chrome(options=self._options)
        self._thread_stack = []
        
    @property
    def driver(self):
        return self._driver
        
    @property
    def has_threads(self):
        return len(self._thread_stack) > 0
        
    def clear_threads(self):
        self._thread_stack.clear()
        
    @property
    def current_thread(self):
        return self._thread_stack[-1] if self.has_threads else None
        
    def push_thread(self, thread):       
        if self.has_threads:
            current = self.current_thread
            current.pause()
        self._thread_stack.append(thread)
        thread.finished.connect(self.pop_thread)
        thread.start()            
    
    def pop_thread(self):
        if self.has_threads:
            finished = self._thread_stack.pop(-1)
            current = self.current_thread
            if current is not None:
                current.resume()    
            return finished            
    

auto_task_runner = None  