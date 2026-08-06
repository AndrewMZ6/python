from threading import Thread
from func_module import my_gen
# TODO:
# to make a function that accepts number of threads a input variable an does some task
# dividing it to a number of threads specified by parameter like this:
# def run_task_using_n_threads(n:int):
# 	split the task to n threads


L = []


def thr(n, name):
    for i in my_gen(n):
        L.append(f"{str(name + 1)} thread::{i}")
    print(f"thread {name} is done!")


threads = []
for _ in range(4):
    t = Thread(target=thr, args=(25, _))
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()

print(len(L))
for i in L:
    print(i)


# output:
# thread 3 is done!
# thread 2 is done!
# thread 1 is done!
# thread 0 is done!
# 100
# 4 thread::davidlloyd@example.org
# 1 thread::byrdjeff@example.org
# 3 thread::vickie64@example.net
# 2 thread::andregarcia@example.net
# 2 thread::christopher61@example.org
# 4 thread::erikapena@example.net
# 3 thread::ellischristy@example.org
# 1 thread::graceolson@example.com
# 4 thread::heatherwebb@example.net
# 2 thread::alex93@example.org
# 1 thread::kimberlymoore@example.net
# 3 thread::randerson@example.net
# 3 thread::jessicagutierrez@example.com
# 4 thread::vvilla@example.com
# 1 thread::evanscarol@example.org
# 2 thread::jeffreywhite@example.org
# 3 thread::qgaines@example.com
# 4 thread::hollyburnett@example.com
# 2 thread::watsondanny@example.com
# 1 thread::jeffreylarsen@example.org
# 3 thread::lindseyedward@example.com
# 4 thread::harrisonnichole@example.org
# 2 thread::lewisheather@example.net
# 1 thread::garciajanet@example.org
# 3 thread::stephanie00@example.com
# 2 thread::jamesschwartz@example.org
# 4 thread::hlopez@example.net
# 1 thread::tyler10@example.net
# 3 thread::matthew12@example.com
# 4 thread::rodrigueznicholas@example.com
# 2 thread::vwilson@example.net
# 1 thread::monicaramos@example.com
# 3 thread::mdelgado@example.net
# 4 thread::stephaniespencer@example.org
# 2 thread::xsmith@example.com
# 1 thread::shellyzimmerman@example.net
# 3 thread::justinjohnson@example.org
# 4 thread::heatherarmstrong@example.com
# 2 thread::richmondelizabeth@example.net
# 1 thread::mcdanielheidi@example.org
# 3 thread::rachel91@example.net
# 4 thread::tperry@example.org
# 2 thread::opeters@example.net
# 1 thread::charlesbird@example.com
# 3 thread::elizabethjones@example.com
# 4 thread::igarcia@example.org
# 2 thread::potterthomas@example.org
# 1 thread::nancywilliams@example.org
# 3 thread::mzamora@example.net
# 4 thread::michaelberry@example.net
# 2 thread::tracy23@example.org
# 1 thread::thomas54@example.com
# 3 thread::ricky20@example.net
# 4 thread::johnsonkaren@example.net
# 2 thread::hartbrandon@example.net
# 1 thread::ubarnes@example.org
# 3 thread::rdavis@example.org
# 2 thread::anthony45@example.net
# 4 thread::gonzaleschristopher@example.com
# 1 thread::michael78@example.org
# 3 thread::khandonald@example.org
# 2 thread::vanessa02@example.com
# 4 thread::joshua50@example.net
# 1 thread::blanchardderrick@example.net
# 3 thread::hurstsarah@example.net
# 4 thread::pauladkins@example.org
# 2 thread::frank96@example.net
# 1 thread::echang@example.net
# 3 thread::scottjones@example.com
# 4 thread::hilljulie@example.com
# 2 thread::greerwilliam@example.com
# 1 thread::melissa45@example.org
# 3 thread::morristeresa@example.net
# 4 thread::kari32@example.net
# 2 thread::cynthia70@example.com
# 1 thread::kdiaz@example.net
# 3 thread::millsbrooke@example.com
# 4 thread::qreeves@example.org
# 2 thread::wreyes@example.org
# 1 thread::qwyatt@example.org
# 4 thread::bradleyperez@example.com
# 3 thread::evansrebecca@example.net
# 2 thread::vperez@example.org
# 1 thread::spencer07@example.net
# 4 thread::justin58@example.net
# 3 thread::eric74@example.org
# 2 thread::znewman@example.org
# 1 thread::fowlerdavid@example.net
# 4 thread::zdean@example.com
# 3 thread::robertsnyder@example.com
# 2 thread::ijoseph@example.com
# 1 thread::trosales@example.com
# 4 thread::gdiaz@example.net
# 3 thread::sotochristian@example.org
# 2 thread::ylambert@example.com
# 1 thread::danielmccormick@example.net
# 4 thread::kingjeff@example.org
# 3 thread::michaelrivera@example.org
# 2 thread::michele98@example.com
# 1 thread::rachel26@example.com
# [Finished in 5.9s]
