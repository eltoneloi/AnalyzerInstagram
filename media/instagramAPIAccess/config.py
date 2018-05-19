# -*- coding: utf-8 -*-

app_authenticate = {'access_token':'',
                    'user_id':'',
        }

base_uri={'get_user':'https://api.instagram.com/v1/users/self/?access_token='+app_authenticate['access_token'],
          'get_media':'https://api.instagram.com/v1/users/self/media/recent/?access_token='+app_authenticate['access_token'],
          'get_comments':'https://api.instagram.com/v1/media/{media-id}/comments?access_token='+app_authenticate['access_token'],
          }