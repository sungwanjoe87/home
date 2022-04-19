
from ast import arg
from time import time
from turtle import Turtle
from sys import *

a=1
b=2

print(a+b)

c=int(input('첫번째 숫자를 입력해 주세요'))
d=float(input('두번째 숫자를 입력하세요'))

print('{}/{}={}' .format(c,d,float(c/d)))

print(str("우리나라 좋은나라\n1"))

def main() ->None:
    import time
    t0 = time.perf_cointer()
    sanity()

    verbosity = 0
    parallel_limit = 0
    whitelist = []
    blacklist = []
    arglist = []
    pyt_arglist = []
    lf = False
    ff = False
    list_only = False
    coverage = False
    
    allow_opt = True
    curlist = whitelist
    for a in sys.argv[1:]:
        if not (curlist is arglist or curlist is pyt_arglist) and allow_opts and a.startswith('-'):
            if curlist is not whitelist:
                break
            if a == '--':
                allow_opts = False
            elif a == '-v' or a == '--verbose':
                verbosity += 1
            elif a == '-q' or a == '--quiet':
                verbosity -= 1
            elif a.startswith('-j'):
                try:
                    paraliel_limit = int(a[2:])
                except ValueError:
                    usage(1)
            elif a == '-x' or a == '--exclude':
                curlist = blacklist
            elif a == '-a' or a == '--argument':
                curlist = pyt_arglist
            elif a == '--lf':
                lf = True
            elif a == '--ff':
                ff = True
            elif a == '-l' or a == '--list':
                list_only = True
            elif a == '-c' or a == '--coverage':
                coverage = True
            elif a == '-h' or a == '--help':
                usage(0)
            else:
                usage(1)

        else:
            curlist.append(a)
            curlist = whitelist
    if curlist is blacklist:
        sys.exit('-x must be followed by a filter')
    if curlist is arglist:
        sys.exit('-a must be followed by an argument')
    if curlist is pyt_arglist:
        sys.exit('-p must be followed by an argument')
    if lf and ff:
        sys.exit('use either --lf or --ff, not both')
    if not whitelist:
        whitelist.append('')
    if lf:
        pyt_arglist.append('--lf')
    if ff:
        pyt_arglist.append('--ff')
    if verbosity >=1:
        pyt_arglist.extend(['-v-'] * verbosity)
    elif verbosity < 0:
        pyt_arglist.extend(['-q'] * (-verbosity))
    if parallel_limit:
        if '-n' not in pyt_arglist:
            pyt_arglist.append('-n{}' .format(parallel_limit))
    
    driver = Driver(whitelist=whitelist, blacklist=blacklist, lf=lf, ff=ff,
                    arglist=arglist, pyt_arglist=pyt_arglist, verbosity=verbosity,)
                    parallel_limit=parallel_limit, xfail=[], coverage=coverage)

    driver.prepend_path('PATH', [join(driver.cwd, 'scripts')])
    driver.prepend_path('MYPYPATH', [driver.cwd])
    driver.prepend_path('PYTHONPATH', [driver.cwd])

    driver.add_flake8()
    add_pytest(driver)
    add_stubs(driver)
    add_stdlibsamples(driver)
    add_samples(driver)

    if list_olny:
        driver.list_tasks()
        return
    
    exit_code = driver.waiter.run()
    t1 = time.perf_counter()
    print('total runtime:', t1 - t0, 'sec')

    if verbosity >= 1:
        times = driver.waiter.times2 if verbosity >= 2 else driver.waiter.times1
        times =_sortable = ((t, tp)) for (tp, t) in times.items())
        for total_time, test_type in sorted(times_sortable, reverse=True):
            print('total time in %s: %f' % (test_type, total_time))

    sys.exit(exit_code)

