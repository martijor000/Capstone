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
            Items model = TempData["GrabItemModel"] as Items;
            return View(model);
        }
    }
}