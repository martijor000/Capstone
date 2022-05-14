using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using WebAPI.Models;

namespace WebAPI.Controllers
{
    public class AccessoryController : ApiController
    {
        public IEnumerable<BabyAccessory> Get()
        {
            using (SafewayBabyAccesoryEntity dbContext = new SafewayBabyAccesoryEntity())
            {
                return dbContext.BabyAccessories.ToList();
            }
        }
        public BabyAccessory Get(int id)
        {
            using (SafewayBabyAccesoryEntity dbContext = new SafewayBabyAccesoryEntity())
            {
                return dbContext.BabyAccessories.FirstOrDefault(e => e.ID == id);
            }
        }


    }
}
