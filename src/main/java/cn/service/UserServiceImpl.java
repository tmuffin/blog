/**
 * 服务实现:用户
 * @author Philip
 */
package cn.muffino.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import cn.muffino.dao.UserDao;
import cn.muffino.model.User;
import cn.muffino.service.UserService;

@Service
public class UserServiceImpl implements UserService {
	@Autowired  
  private UserDao userDao;  

  public User selectUserById(Integer userId) {  
    return userDao.selectUserById(userId);
  } 
}
