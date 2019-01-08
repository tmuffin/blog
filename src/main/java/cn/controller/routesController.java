/**
 * 控制器: 路由
 * @author Philip
 */
package cn.muffino.controller;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class RoutesController {
  @Resource  
  private UserService userService;  

  @RequestMapping("/login")    
  public ModelAndView getIndex () {      
    ModelAndView modelView = new ModelAndView("login");
    User user = userService.selectUserById(1);

    modelView.addObject("user", user);
    return modelView;
  }

  @RequestMapping("/")    
  public ModelAndView getIndex () {      
    ModelAndView modelView = new ModelAndView("index");
    User user = userService.selectUserById(1);

    modelView.addObject("user", user);
    return modelView;
  }
}
