# -*- coding: utf-8 -*-

#Instagram do Coxinha
'''app_authenticate = {'access_token':'2353444484.8cd1b31.dd3879c710d24dc08b87bfa9720bbce1',
                    'user_id':'2353444484',
        }'''


#Instagram do Lucas
app_authenticate = {'access_token':'618642185.93c63ab.43a8effd4d7a44bb80e93040904a7fed',
                    'user_id':'618642185',
        }

base_uri={'get_user':'https://api.instagram.com/v1/users/self/?access_token='+app_authenticate['access_token'],
          'get_media':'https://api.instagram.com/v1/users/self/media/recent/?access_token='+app_authenticate['access_token'],
          'get_comments':'https://api.instagram.com/v1/media/{media-id}/comments?access_token='+app_authenticate['access_token'],
          }