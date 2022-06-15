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
            List<double?> tempSinglePrices = TempData["GrabSinglePrices"] as List<double?>;
            List<int> multiplier = new List<int>();

            double? totalPrice = 0;
            for(int i = 0; i < tempPrices.Count; i++)
            {
                multiplier.Add(Convert.ToInt32(tempPrices[i] / tempSinglePrices[i]));
                totalPrice += tempPrices[i];
            }
            TempData["TotalPrice"] = totalPrice;
            TempData["Multiplier"] = multiplier; 
            return View();
        }
    }
}