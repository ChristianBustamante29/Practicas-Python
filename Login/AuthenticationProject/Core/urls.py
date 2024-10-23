from django.urls import path
from . import views
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea

urlpatterns = [
    path('', ListaPendientes.as_view(), name='home'),
    path('register/', views.RegisterView, name="register"),
    path('login', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
    path('forgot-password/', views.ForgotPassword, name="forgot-password"),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name="password-reset-sent"),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name="reset-password"),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
    path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
    path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea'),
]
