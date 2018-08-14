package cn.steudnera.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import cn.steudnera.dao.UserDao;
import cn.steudnera.model.User;
import cn.steudnera.service.UserService;

@Service
public class UserServiceImpl implements UserService {
  @Autowired
  private UserDao userDao;

  public User selectUserById (Integer userId) {
    return userDao.selectUserById(userId);
  }
}
