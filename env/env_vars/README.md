In any working environment this directory needs to contain a file named 
.env. This file holds sensitive environment variables that must not be 
distributed in GIT.

Remember to chmod this file to something very restrictive. It needs to be 
readable by the user under which the WSGI server runs. In case of webfaction 
this user is the system user, which makes 400 appropriate.

    $ chmod 400 ./.env
    
**Example**

You can copy this code, rename the attributes and save it to ./.env. 

    #!/bin/bash
    DJ_PROJECT_CURRENT_ENV=""
    
    DJ_PROJECT_DEV_SECRET_KEY=""
    DJ_PROJECT_DEV_DB_NAME=""
    DJ_PROJECT_DEV_DB_USER=""
    DJ_PROJECT_DEV_DB_HOST=""
    DJ_PROJECT_DEV_DB_PASS=""
    
    DJ_PROJECT_DEV_CELERY_USER=""
    DJ_PROJECT_DEV_CELERY_PASS=""
    DJ_PROJECT_DEV_CELERY_HOST=""
    DJ_PROJECT_DEV_CELERY_PORT=""
    
    DJ_PROJECT_DEV_SERVER_EMAIL=""
    DJ_PROJECT_DEV_EMAIL_BACKEND=""
    DJ_PROJECT_DEV_EMAIL_HOST=""
    DJ_PROJECT_DEV_EMAIL_PORT=""
    DJ_PROJECT_DEV_EMAIL_HOST_USER=""
    DJ_PROJECT_DEV_EMAIL_HOST_PASSWORD=""
    DJ_PROJECT_DEV_EMAIL_USE_TLS=""