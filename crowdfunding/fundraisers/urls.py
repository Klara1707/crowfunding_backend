
from django.urls import path
from .views import FundraiserList, FundraiserDetail, PledgeList, PledgeDetail

urlpatterns = [
    # Fundraiser endpoints
    path('fundraisers/', FundraiserList.as_view(), name='fundraiser-list'),
    path('fundraisers/<int:pk>/', FundraiserDetail.as_view(), name='fundraiser-detail'),

    # Pledge endpoints
    path('pledges/', PledgeList.as_view(), name='pledge-list'),
    path('pledges/<int:pk>/', PledgeDetail.as_view(), name='pledge-detail'),
]


