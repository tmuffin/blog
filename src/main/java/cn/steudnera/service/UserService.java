package cn.steudnera.service;
import cn.steudnera.model.User;

public interface UserService {
	User selectUserById(Integer userId);
}
