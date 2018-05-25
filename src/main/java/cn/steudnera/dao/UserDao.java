package cn.steudnera.dao;

import cn.steudnera.model.User;

public interface UserDao {
	public User selectUserById(Integer userId);  
}
