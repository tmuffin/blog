package cn.muffino.service;

import cn.muffino.model.User;

public interface UserService {
	User selectUserById(Integer userId);
}
