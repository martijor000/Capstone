using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using TypeNSaveWebForm.Models.Safeway.Baby;

namespace TypeNSaveWebForm.Controllers.SafewayControllers.Baby
{
    public class AccessoryController : Controller
    {
        public IEnumerable<BabyAccessory> Get()
        {
            using (SafewayBabyAccEntities dbContext = new SafewayBabyAccEntities())
            {
                return dbContext.BabyAccessories.ToList();
            }
        }
        public BabyAccessory Get(int id)
        {
            using (SafewayBabyAccEntities dbContext = new SafewayBabyAccEntities())
            {
                return dbContext.BabyAccessories.FirstOrDefault(e => e.ID == id);
            }
        }
    }
}