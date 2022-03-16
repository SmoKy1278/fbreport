import re, random, time, bs4, os, sys, mechanize,requests
from http.cookiejar import LWPCookieJar as kuki
os.system('clear')
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_cookiejar(kuki())
br.addheaders = [
        (
          'User-Agent',
          random.choice(open('useragents.txt').read().splitlines()))]
filee = 'ids.txt'
def report():
    url = ('https://m.facebook.com/login.php')
    email = input('[#] Enter Email: ')
    passwr= input('[#] Enter Password: ')

    br.open(url)
    br.select_form(nr=0)
    br.form['email'] = ('{}').format(email)
    br.form['pass'] = ('{}').format(passwr)
    br.submit()
    if 'save-device' in br.geturl():
        print('[#] Login success ')
        id=input('[#] Username Target : ')
        my = ('https://m.facebook.com/' + id)
        url = my
        br.open(url)
        r=re.findall('<title>(.*?)</title>', br.response().read().decode('utf-8'))
        if len(r) != 0:
            dray = input('[#] Enter Untuk Melanjutkan  ')
            uoh = open(filee, 'r')
            uhoh = uoh.read()
            if id in uhoh:
                print('.         Oops 405')
                exit('You have already reported this account using the account you used')
            else:
                bs = br.response().read()
                bb = bs4.BeautifulSoup(bs, features='html.parser') 
                if len(bb) != 0:
                    for x in bb.find_all('a', href=True):
                        if 'rapid_report' in x['href']:
                            cadow = x['href']
                            br.open(cadow)
                            try:
                                br._factory.is_html = True
                                br.select_form(nr=0)
                                br.form['tag'] = ['profile_fake_account']
                                br.submit()
                            except Exception as f:
                                print(f)
                                print ('    Bad406')
                            try:
                                br._factory.is_html = True
                                br.select_form(nr=0)
                                br.form['action_key'] = ['FRX_PROFILE_REPORT_CONFIRMATION']
                                br.submit()
                            except Exception as f:
                                print(f)
                                print ('    Bad406')
                            try:
                                br._factory.is_html = True
                                br.select_form(nr=0)
                                br.form['checked'] = ['yes']
                                br.submit()
                                jj = open(filee, 'w')
                                jj.write(id)
                                time.sleep(2)
                                print('[#] Sukses Reported')
                                time.sleep(1)
                                exit()
                            except Exception as f:
                                print(f)
                                print ('    Bad406')
    else:
        exit('[#] FAILED INTO LOGIN IN YOUR ACCOUNT ')
if __name__ == '__main__':
    report()
