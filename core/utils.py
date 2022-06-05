"""
Created on 05-Jun-2022
@author: Abdulkadir
"""
from rest_framework.response import Response
from rest_framework import status


def response(response, response_status=None):
    '''
    @summary: response is a utility function to output the final JSON response
        created using the params

    @param response: dict
    @param response_status: int
    @return: Response object
    '''
    if not response_status:
        response_status = status.HTTP_200_OK
    if 200 <= response_status <= 207:
        response = {
            "success": True,
            "result": response,
        }
    else:
        response = {
            "success": False,
            "result": response,
        }
    return Response(response, status=response_status, headers={'Content-Type': 'application/json',
                                                               })
