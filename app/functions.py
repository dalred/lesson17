def set_keys(req_json, inst_cls):
    inst_cls_keys = [key for key in inst_cls.__dict__.keys() if key != '_sa_instance_state']
    for k, v in req_json.items():
        #Проверка в принципе не нужна,
        # потому что Flask сам обработает,
        # если ключ в json отличный от схемы.
        if k in inst_cls_keys:
            setattr(inst_cls, k, v)