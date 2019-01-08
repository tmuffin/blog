/**
 * 控制器: 附件
 * @author Philip
 */
package cn.muffino.controller;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import cn.model.Attachment;
import cn.service.AttachmentController;

@Controller
public class AttachmentController {
  @Resource  
  private UserService userService;  

  @RequestMapping("/showUserInfo")    
  public ModelAndView getIndex () {      
    ModelAndView modelView = new ModelAndView("index");
    User user = userService.selectUserById(1);

    modelView.addObject("user", user);
    return modelView;
  } 
}
