from user import Admin

admin = Admin('jonas', 'jon', 'jonas@outlook.com', 'jonas123', '123')
admin.describe_user()
admin.privilages = [
                    'pode adicionar post',
                    'pode deletar post',
                    'pode banir usuario'
                    ]
admin.show_privilages()