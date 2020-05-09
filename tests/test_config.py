from catsleep.cat import config as cfg 


if __name__ == '__main__':
    conf = cfg.Config()
    
    try:
        print('user configurations:')
        print(conf.get_user_config())
    except Exception as e:
        print('default configurations:')
        print(conf.get_default_config())