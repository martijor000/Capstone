//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace TypeNSaveWebForm.Models.Safeway.Baby
{
    using System;
    using System.Data.Entity;
    using System.Data.Entity.Infrastructure;
    
    public partial class SafewayBabyBathEntity : DbContext
    {
        public SafewayBabyBathEntity()
            : base("name=SafewayBabyBathEntity")
        {
        }
    
        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            throw new UnintentionalCodeFirstException();
        }
    
        public virtual DbSet<BabyBathsAndSkinCare> BabyBathsAndSkinCares { get; set; }
    }
}
