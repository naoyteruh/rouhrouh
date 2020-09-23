from fabric.api import local, run, cd, env, prefix 

REMOTE_WORKING_DIR = '/home/superman/.virtualenvs/ekiLibr/projects/rouhrouh/'
env.hosts = ['95.142.165.76'] 
#env.user = 'superman'
env.user = 'root'

def deploy():
  #local("python ../../manage.py collectstatic --clear --noinput")
  local("hg pull")
  local("hg addremove")
  local("hg commit")
  local("hg push")
  with cd(REMOTE_WORKING_DIR):
    with prefix('workon ekiLibr'):            
      run("hg pull")
      run("hg update")
      run("chmod -R 777 var")
      run("chmod -R 777 medias")
      run("./manage.py collectstatic --clear --noinput")
      #run("./manage.py collectstatic --noinput")
      run("service apache2 reload")