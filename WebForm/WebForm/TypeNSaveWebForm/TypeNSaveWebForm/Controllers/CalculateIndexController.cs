using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using TypeNSaveWebForm.Models.Universal;

namespace TypeNSaveWebForm.Controllers
{
    public class CalculateIndexController : Controller
    {
        // GET: CalculateIndex
        public ActionResult Index()
        {
            List<string> tempProducts = TempData["GrabItemProducts"] as List<string>;
            List<double?> tempPrices = TempData["GrabItemPrices"] as List<double?>;
            return View();
        }
    }
}