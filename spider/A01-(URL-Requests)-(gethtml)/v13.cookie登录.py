from urllib import request

if __name__ == '__main__':

    url = 'http://www.renren.com/967544458/profile'

    headers ={
        'Cookie' :'anonymid=jkxkpbvhosk3hx; depovince=BJ; _r01_=ce1; JSESSIONID=abc6AD3oVAgu2_e_BBgvw; ick_login=fea8baf9-d884-4fcc-9368-cb463afdf6c4; t=d71cd9e57474f0515bb4e1c06371c66d8; societyguester=d71cd9e57474f0515bb4e1c06371c66d8; id=967544458; xnsid=b991e1dc; ver=7.0; loginfrom=null; jebe_key=d0fae8c2-859b-426f-a657-3af460b088d1%7C550a369c88033a06418d4a595f6f1b36%7C1534485323659%7C1; jebecookies=a394cc80-ce6d-4d7e-b190-83b8520c64a3|||||; wp_fold=0; jebe_key=d0fae8c2-859b-426f-a657-3af460b088d1%7C550a369c88033a06418d4a595f6f1b36%7C1534485323659%7C1%7C1534487791519'
    }

    req= request.Request(url, headers= headers)

    rsq = request.urlopen(req)

    html = rsq.read().decode()

    with open (r"/home/tlxy/PCM/rccode/spliderexe/htmlcf/"+'使用cookie登录' +'.html','w') as f:
        f.write(html)

