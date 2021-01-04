from admin import Admin

#cadastrando
admin = Admin('jonas',
              'jones',
              'jonas@outlook.com',
              'jonas123',
              '123')


# atribuindo privilegios
admin.privilages.privilages = [
                    'pode adicionar post',
                    'pode deletar post',
                    'pode banir usuario'
                    ]

#=-=-=-=-mostrando =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

admin.describe_user()

admin.privilages.show_privilages()