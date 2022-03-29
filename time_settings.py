from datetime import datetime
import time
import requests
import gc

log_list = []

class work:
    def __init__(self,start_d, start_h, start_m, end_d, end_h, end_m):
        self.start_d = start_d
        self.start_h = start_h
        self.start_m = start_m
        self.end_d = end_d
        self.end_h = end_h
        self.end_m = end_m

    def log(self, param):
        global log_list
        with open('./Stability_training_platform.txt', mode='a', encoding='utf-8') as f:
            data = param
            f.write(data + '\n')

        
    def workfunc(self):
        r = requests.get('http://192.168.5.181:5000/auth/login')
        print('*'*10)
        print('執行時間: ', str(datetime.now()))
        print('Status Code:', r.status_code)
        print('*'*10)
        gc.collect()

    def main(self):
        now = datetime.now()
        # Start condition
        condition = now.day == int(self.start_d) and now.hour == int(self.start_h) and now.minute == int(self.start_m)
        while condition:
            if now.day == int(self.end_d) and now.hour == int(self.end_h) and now.minute == int(self.end_m):
                break
            elif now.hour == int('17'):
                time.sleep(57600)
            else:
                self.workfunc()
                time.sleep(720)
            print('Finish')

if __name__ == '__main__':
    func = work('10', '10', '19', '10', '12', '14')
    func.main()
