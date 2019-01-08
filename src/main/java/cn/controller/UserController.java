/**
 * 控制器: 用户
 * @author Philip
 */
package cn.muffino.controller;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import cn.model.User;
import cn.service.UserService;

@Controller
public class UserController {
  @Resource
  private UserService userService;  

  @RequestMapping("/user")    
  public ModelAndView getIndex () {      
    ModelAndView mav = new ModelAndView("index");
    User user = userService.selectUserById(1);

    mav.addObject("user", user);
    return mav;
  } 
}
