from django.urls import path
from core import views
app_name="core"
from core import transaction
from core import transfer

from core import payment_request

app_name="core"
from  core import credit_card
urlpatterns=[
    path("",views.index,name="index"),
    # Transfers


    path("search-account/",transfer.search_users_account_number,name="search-account"),
    path("amount-transfer/<account_number>/",transfer.AmountTransfer,name="amount-transfer"),
    path("amount-transfer-process/<account_number>/",transfer.AmountTransferProcess,name="amount-transfer-process"),
    path("transfer-confirmation/<account_number>/<transaction_id>",transfer.TransferConfirmation,name="transfer-confirmation"),
    path("transfer-process/<account_number>/<transaction_id>",transfer.TransferProcess,name="transfer-process"),
    path("transfer-completed/<account_number>/<transaction_id>",transfer.TransferCompleted,name="transfer-completed"),
    




    #transactions

    path("transactions/",transaction.transaction_lists,name="transactions"),
    path("transaction-detail/<transaction_id>/",transaction.transaction_detail,name="transaction-detail"),


    #request  money

    #payment request urls 
    path("request-search-account/",payment_request.SearchUsersRequest,name="request-search-account"),
    path("amount-request/<account_number>",payment_request.AmountRequest,name="amount-request"),
    path("amount-request-process/<account_number>",payment_request.AmountRequestProcess,name="amount-request-process"),
    path("amount-request-confirmation/<account_number>/<transaction_id>/",payment_request.AmountRequestConfirmation,name="amount-request-confirmation"),
    path("amount-request-final-process/<account_number>/<transaction_id>/",payment_request.AmountRequestFinalProcess,name="amount-request-final-process"),
    path("amount-request-completed/<account_number>/<transaction_id>/",payment_request.RequestCompleted,name="amount-request-completed"),



    # settlement urls
    # request settlement
    path("settlement-confirmation/<account_number>/<transaction_id>/",payment_request.settlement_confirmation,name="settlement-confirmation"),
    path("settlement-processing/<account_number>/<transaction_id>/",payment_request.settlement_processing,name="settlement-processing"),
    path("settlement-completed/<account_number>/<transaction_id>/",payment_request.SettlementCompleted,name="settlement-completed"),
    path("delete-request/<account_number>/<transaction_id>/",payment_request.deletePaymentRequest,name="delete-request"),
    # you should be consistent in  your naming conventions


    

    #Credit Card Details Urls
    path("card/<card_id>/",credit_card.card_detail,name="card-detail"),
    path("fund-credit-card/<card_id>/",credit_card.fund_credit_card,name="fund-credit-card"),
    path("withdraw_fund/<card_id>/",credit_card.withdraw_fund,name="withdraw_fund"),
    path("delete_card/<card_id>/",credit_card.delete_card,name="delete_card"),


]