from django.shortcuts import render
from unicodedata import category
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
import numpy as np

from models import User
# Create your views here.

class Views_Controls(View):

    def post(self, request):

        user = {}
        post_len = 0
        follower_len = 0
        user_type = 'my'
        is_follow = False
        estimationData = []
        trainingName = []
        achievement_rate = 0
        estimationName = ['5m 셔틀런','10m 셔틀런','박스 점프','롱 점프','사이드 스텝']
        estimationData = [{
            'id': '1',
            'date': '2022-07-10',
            'category': '1',
        },{
            'id': '2',
            'date': '2022-08-01',
            'category': '2',
        },{
            'id': '3',
            'date': '2022-01-01',
            'category': '3',
        },{
            'id': '4',
            'date': '2022-08-02',
            'category': '2',
        },{
            'id': '5',
            'date': '2022-08-01',
            'category': '5',
        },{
            'id': '6',
            'date': '2022-08-05',
            'category': '1',
        },{
            'id': '7',
            'date': '2022-08-08',
            'category': '1',
        },
        ]
        trainingData = []
        
        

        # 내 정보일 떄
        if request.POST['user_id'] == str(request.session['id']):
            user = User.objects.get(pk=request.session['id'])
            # estimationData = Estimation.objects.filter(user_id=request.session['id'])
            # trainingData = Training.objects.filter(user_id=request.session['id'])
            
        # 다른 유저 정보일 떄
        else:
            user = User.objects.get(pk=request.POST['user_id'])
            user_type = 'others'
            
        
        achievement_rate = self.achievementrate(estimationData, 5)
        categorylist = self.listtocategory(estimationData)
        passdate = self.passdate(estimationData)
        
        print(estimationData[0]['category'])
        
        context = {
            'user': user,
            'post_len': post_len,
            'follower_len': follower_len,
            'user_id': request.POST['user_id'],
            'user_type': user_type,
            'is_follow': is_follow,
            'estimation': estimationData,
            'estimation_name': estimationName,
            'achievement_rate': achievement_rate,
            'categorylist': categorylist,
            'training': trainingData,
            'passdate': passdate,
        }

        return render(request, 'app_www/user/index.html', context)

    def achievementrate(self, Datas, category_num):
        array = np.zeros(category_num)
        for Data in Datas:
            array[int(Data['category'])-1] = 1
        sum = np.sum(array)
        
        return sum/category_num
    
    def listtocategory(self, Datas):
        ret = []
        for i in range(len(Datas)):
            ret.append(int(Datas[i]['category']))
        return ret
    
    def passdate(self, Datas):
        ret = []
        for i in range(len(Datas)):
            ret.append(Datas[i]['date'])
        return ret