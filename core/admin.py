def admin_run():
    def register():
        pass
    def change_balance():
        pass
    def lock():
        pass
    admin_dict={
        '1':register,
        '2':change_balance,
        '3':lock,
    }
    while True:
        print(
            '''
            1. 创建账户
            2. 修改余额
            3. 冻结账户
            '''
        )

    return None