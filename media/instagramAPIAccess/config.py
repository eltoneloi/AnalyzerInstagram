# -*- coding: utf-8 -*-

app_authenticate = {'access_token':'2353444484.8cd1b31.dd3879c710d24dc08b87bfa9720bbce1',
                    'user_id':'2353444484',
        }

base_uri={'get_user':'https://api.instagram.com/v1/users/self/?access_token='+app_authenticate['access_token'],
          'get_media':'https://api.instagram.com/v1/users/self/media/recent/?access_token='+app_authenticate['access_token'],
          'get_comments':'https://api.instagram.com/v1/media/{media-id}/comments?access_token='+app_authenticate['access_token'],
          }