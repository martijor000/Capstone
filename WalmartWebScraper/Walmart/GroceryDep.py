
import requests
import json
import pandas as pd
import time
from sqlalchemy import create_engine, false, true

import requests
import json

url = "https://www.walmart.com/orchestra/home/graphql/browse?affinityOverride=default&page=1&prg=desktop&catId=976759_9176907_4405816&sort=best_match&ps=40&searchArgs.cat_id=976759_9176907_4405816&searchArgs.prg=desktop&fetchMarquee=true&fetchSkyline=true&fetchSbaTop=false&enablePortableFacets=true&tenant=WM_GLASS"

payload = json.dumps({
  "query": "query Browse( $query:String $page:Int $prg:Prg! $facet:String $sort:Sort $catId:String! $max_price:String $min_price:String $module_search:String $affinityOverride:AffinityOverride $ps:Int $ptss:String $beShelfId:String $fitmentFieldParams:JSON ={}$fitmentSearchParams:JSON ={}$rawFacet:String $seoPath:String $trsp:String $fetchMarquee:Boolean! $fetchSkyline:Boolean! $additionalQueryParams:JSON ={}$enablePortableFacets:Boolean = false $tenant:String! ){search( query:$query page:$page prg:$prg facet:$facet sort:$sort cat_id:$catId max_price:$max_price min_price:$min_price module_search:$module_search affinityOverride:$affinityOverride additionalQueryParams:$additionalQueryParams ps:$ps ptss:$ptss trsp:$trsp _be_shelf_id:$beShelfId ){query searchResult{...BrowseResultFragment}}contentLayout( channel:\"WWW\" pageType:\"BrowsePage\" tenant:$tenant version:\"v1\" searchArgs:{query:$query cat_id:$catId _be_shelf_id:$beShelfId prg:$prg}){modules{...ModuleFragment configs{...on EnricherModuleConfigsV1{zoneV1}__typename...on _TempoWM_GLASSWWWSearchSortFilterModuleConfigs{facetsV1 @skip(if:$enablePortableFacets){...FacetFragment}topNavFacets @include(if:$enablePortableFacets){...FacetFragment}allSortAndFilterFacets @include(if:$enablePortableFacets){...FacetFragment}}...on TempoWM_GLASSWWWPillsModuleConfigs{moduleSource pillsV2{...PillsModuleFragment}}...TileTakeOverProductFragment...on TempoWM_GLASSWWWSearchFitmentModuleConfigs{fitments( fitmentSearchParams:$fitmentSearchParams fitmentFieldParams:$fitmentFieldParams ){...FitmentFragment sisFitmentResponse{...BrowseResultFragment}}}...on TempoWM_GLASSWWWStoreSelectionHeaderConfigs{fulfillmentMethodLabel storeDislayName}...on TempoWM_GLASSWWWSponsoredProductCarouselConfigs{_rawConfigs}...PopularInModuleFragment...CopyBlockModuleFragment...BannerModuleFragment...HeroPOVModuleFragment...InlineSearchModuleFragment...MarqueeDisplayAdConfigsFragment @include(if:$fetchMarquee)...SkylineDisplayAdConfigsFragment @include(if:$fetchSkyline)...HorizontalChipModuleConfigsFragment}}...LayoutFragment pageMetadata{location{pickupStore deliveryStore intent postalCode stateOrProvinceCode city storeId accessPointId accessType}pageContext}}seoBrowseMetaData( id:$catId facets:$rawFacet path:$seoPath facet_query_param:$facet _be_shelf_id:$beShelfId ){metaTitle metaDesc metaCanon h1}}fragment BrowseResultFragment on SearchInterface{title aggregatedCount...BreadCrumbFragment...ShelfDataFragment...DebugFragment...ItemStacksFragment...PageMetaDataFragment...PaginationFragment...RequestContextFragment...ErrorResponse modules{facetsV1 @skip(if:$enablePortableFacets){...FacetFragment}topNavFacets @include(if:$enablePortableFacets){...FacetFragment}allSortAndFilterFacets @include(if:$enablePortableFacets){...FacetFragment}pills{...PillsModuleFragment}}}fragment ModuleFragment on TempoModule{name version type moduleId schedule{priority}matchedTrigger{zone}}fragment LayoutFragment on ContentLayout{layouts{id layout}}fragment BreadCrumbFragment on SearchInterface{breadCrumb{id name url}}fragment ShelfDataFragment on SearchInterface{shelfData{shelfName shelfId}}fragment DebugFragment on SearchInterface{debug{sisUrl adsUrl}}fragment ItemStacksFragment on SearchInterface{itemStacks{displayMessage meta{adsBeacon{adUuid moduleInfo max_ads}query stackId stackType title layoutEnum totalItemCount totalItemCountDisplay viewAllParams{query cat_id sort facet affinityOverride recall_set min_price max_price}}itemsV2{...ItemFragment...InGridMarqueeAdFragment...TileTakeOverTileFragment}}}fragment ItemFragment on Product{__typename id usItemId fitmentLabel name checkStoreAvailabilityATC seeShippingEligibility brand type shortDescription imageInfo{...ProductImageInfoFragment}canonicalUrl externalInfo{url}itemType category{path{name url}}badges{flags{...on BaseBadge{key text type id}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{...on BaseBadge{key text type}}}classType averageRating numberOfReviews esrb mediaRating salesUnitType sellerId sellerName hasSellerBadge availabilityStatusV2{display value}groupMetaData{groupType groupSubType numberOfComponents groupComponents{quantity offerId componentType productDisplayName}}productLocation{displayValue aisle{zone aisle}}fulfillmentSpeed offerId preOrder{...PreorderFragment}priceInfo{...ProductPriceInfoFragment}variantCriteria{...VariantCriteriaFragment}snapEligible fulfillmentBadge fulfillmentTitle fulfillmentType brand manufacturerName showAtc sponsoredProduct{spQs clickBeacon spTags}showOptions showBuyNow rewards{eligible state minQuantity rewardAmt promotionId selectionToken cbOffer term expiry description}}fragment ProductImageInfoFragment on ProductImageInfo{thumbnailUrl}fragment ProductPriceInfoFragment on ProductPriceInfo{priceRange{minPrice maxPrice}currentPrice{...ProductPriceFragment}wasPrice{...ProductPriceFragment}unitPrice{...ProductPriceFragment}listPrice{...ProductPriceFragment}shipPrice{...ProductPriceFragment}subscriptionPrice{priceString subscriptionString}priceDisplayCodes{priceDisplayCondition finalCostByWeight submapType}}fragment PreorderFragment on PreOrder{isPreOrder preOrderMessage preOrderStreetDateMessage}fragment ProductPriceFragment on ProductPrice{price priceString}fragment VariantCriteriaFragment on VariantCriterion{name type id isVariantTypeSwatch variantList{id images name rank swatchImageUrl availabilityStatus products selectedProduct{canonicalUrl usItemId}}}fragment InGridMarqueeAdFragment on MarqueePlaceholder{__typename type moduleLocation lazy}fragment TileTakeOverTileFragment on TileTakeOverProductPlaceholder{__typename type tileTakeOverTile{span title subtitle image{src alt}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title}ctaType ctaTextColor}}}fragment PageMetaDataFragment on SearchInterface{pageMetadata{storeSelectionHeader{fulfillmentMethodLabel storeDislayName}title canonical description location{addressId}}}fragment PaginationFragment on SearchInterface{paginationV2{maxPage pageProperties}}fragment RequestContextFragment on SearchInterface{requestContext{vertical isFitmentFilterQueryApplied searchMatchType categories{id name}}}fragment ErrorResponse on SearchInterface{errorResponse{correlationId source errorCodes errors{errorType statusCode statusMsg source}}}fragment PillsModuleFragment on PillsSearchInterface{title url image:imageV1{src alt}}fragment BannerModuleFragment on TempoWM_GLASSWWWSearchBannerConfigs{moduleType viewConfig{title image imageAlt displayName description url urlAlt appStoreLink appStoreLinkAlt playStoreLink playStoreLinkAlt}}fragment PopularInModuleFragment on TempoWM_GLASSWWWPopularInBrowseConfigs{seoBrowseRelmData(id:$catId){relm{id name url}}}fragment CopyBlockModuleFragment on TempoWM_GLASSWWWCopyBlockConfigs{copyBlock(id:$catId){cwc}}fragment FacetFragment on Facet{title name type layout min max selectedMin selectedMax unboundedMax stepSize isSelected values{id name description type itemCount isSelected baseSeoURL}}fragment FitmentFragment on Fitments{partTypeIDs result{status formId position quantityTitle extendedAttributes{...FitmentFieldFragment}labels{...LabelFragment}resultSubTitle notes suggestions{...FitmentSuggestionFragment}}labels{...LabelFragment}savedVehicle{vehicleYear{...VehicleFieldFragment}vehicleMake{...VehicleFieldFragment}vehicleModel{...VehicleFieldFragment}additionalAttributes{...VehicleFieldFragment}}fitmentFields{...VehicleFieldFragment}fitmentForms{id fields{...FitmentFieldFragment}title labels{...LabelFragment}}}fragment LabelFragment on FitmentLabels{ctas{...FitmentLabelEntityFragment}messages{...FitmentLabelEntityFragment}links{...FitmentLabelEntityFragment}images{...FitmentLabelEntityFragment}}fragment FitmentLabelEntityFragment on FitmentLabelEntity{id label}fragment VehicleFieldFragment on FitmentVehicleField{id label value}fragment FitmentFieldFragment on FitmentField{id displayName value extended data{value label}dependsOn}fragment FitmentSuggestionFragment on FitmentSuggestion{id position loadIndex speedRating searchQueryParam labels{...LabelFragment}cat_id fitmentSuggestionParams{id value}}fragment HeroPOVModuleFragment on TempoWM_GLASSWWWHeroPovConfigsV1{povCards{card{povStyle image{mobileImage{...TempoCommonImageFragment}desktopImage{...TempoCommonImageFragment}}heading{text textColor textSize}subheading{text textColor}detailsView{backgroundColor isTransparent}ctaButton{button{linkText clickThrough{value}uid}}legalDisclosure{regularText shortenedText textColor textColorMobile legalBottomSheetTitle legalBottomSheetDescription}logo{...TempoCommonImageFragment}links{link{linkText}}}}}fragment TempoCommonImageFragment on TempoCommonImage{src alt assetId uid clickThrough{value}}fragment InlineSearchModuleFragment on TempoWM_GLASSWWWInlineSearchConfigs{headingText placeholderText}fragment MarqueeDisplayAdConfigsFragment on TempoWM_GLASSWWWMarqueeDisplayAdConfigs{_rawConfigs ad{...DisplayAdFragment}}fragment DisplayAdFragment on Ad{...AdFragment adContent{type data{__typename...AdDataDisplayAdFragment}}}fragment AdFragment on Ad{status moduleType platform pageId pageType storeId stateCode zipCode pageContext moduleConfigs adsContext adRequestComposite}fragment AdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment SkylineDisplayAdConfigsFragment on TempoWM_GLASSWWWSkylineDisplayAdConfigs{_rawConfigs ad{...SkylineDisplayAdFragment}}fragment SkylineDisplayAdFragment on Ad{...SkylineAdFragment adContent{type data{__typename...SkylineAdDataDisplayAdFragment}}}fragment SkylineAdFragment on Ad{status moduleType platform pageId pageType storeId stateCode zipCode pageContext moduleConfigs adsContext adRequestComposite}fragment SkylineAdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment HorizontalChipModuleConfigsFragment on TempoWM_GLASSWWWHorizontalChipModuleConfigs{chipModuleSource:moduleSource chipModule{title url{linkText title clickThrough{type value}}}chipModuleWithImages{title url{linkText title clickThrough{type value}}image{alt clickThrough{type value}height src title width}}}fragment TileTakeOverProductFragment on TempoWM_GLASSWWWTileTakeOverProductConfigs{TileTakeOverProductDetails{span dwebPosition mwebPosition title subtitle image{src alt}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title}ctaType ctaTextColor}}}",
  "variables": {
    "id": "",
    "affinityOverride": "default",
    "dealsId": "",
    "query": "",
    "page": 6,
    "prg": "desktop",
    "catId": "976759_9176907_4405816",
    "facet": "",
    "sort": "best_match",
    "rawFacet": "",
    "seoPath": "",
    "ps": 40,
    "ptss": "",
    "trsp": "",
    "beShelfId": "",
    "recall_set": "",
    "module_search": "",
    "min_price": "",
    "max_price": "",
    "storeSlotBooked": "",
    "additionalQueryParams": {
      "hidden_facet": None,
      "translation": None
    },
    "searchArgs": {
      "query": "",
      "cat_id": "976759_9176907_4405816",
      "prg": "desktop",
      "facet": ""
    },
    "fitmentFieldParams": None,
    "fitmentSearchParams": {
      "id": "",
      "affinityOverride": "default",
      "dealsId": "",
      "query": "",
      "page": 6,
      "prg": "desktop",
      "catId": "976759_9176907_4405816",
      "facet": "",
      "sort": "best_match",
      "rawFacet": "",
      "seoPath": "",
      "ps": 40,
      "ptss": "",
      "trsp": "",
      "beShelfId": "",
      "recall_set": "",
      "module_search": "",
      "min_price": "",
      "max_price": "",
      "storeSlotBooked": "",
      "additionalQueryParams": {
        "hidden_facet": None,
        "translation": None
      },
      "searchArgs": {
        "query": "",
        "cat_id": "976759_9176907_4405816",
        "prg": "desktop",
        "facet": ""
      },
      "cat_id": "976759_9176907_4405816",
      "_be_shelf_id": ""
    },
    "fetchMarquee": True,
    "fetchSkyline": True,
    "fetchSbaTop": False,
    "enablePortableFacets": True,
    "tenant": "WM_GLASS"
  }
})
headers = {
  'authority': 'www.walmart.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': 'QuantumMetricUserID=1c34634a43bc06585c086015cf1116ee; ACID=aa9205f9-5d45-4951-8293-30a8fdc48cdb; hasACID=true; assortmentStoreId=3531; hasLocData=1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; vtc=WHMuN-dcOBqeI-JqQXna-U; bstc=WHMuN-dcOBqeI-JqQXna-U; mobileweb=0; xpa=0Nd9e|0t4gT|1jR7v|6Yrc-|8wp7a|9DjTL|9Lv_9|LTD5Y|OBldi|ObD24|QnZNm|Umo04|Zm3yB|bupnU|cfVAR|duBe9|eJ9VH|eXnIH|gVG-b|gynZP|hGNr-|hQziI|obzLE|sGDe9|srerY|viJr2|xCzID; exp-ck=0Nd9e10t4gT11jR7v16Yrc-18wp7a29Lv_92Zm3yB2eJ9VH2eXnIH1gVG-b1gynZP2hGNr-1hQziI2obzLE1; TS013ed49a=01538efd7ccbe491c1206d0035eb870503d13c5e63d4d4bc3ff1da836db5384f4036ffde1361b022b6a4927c6d263f879b82c9e76f; TBV=7; dimensionData=979; adblocked=false; pxcts=3cb76c42-e53c-11ec-8057-466159665459; _pxvid=3cb763c5-e53c-11ec-8057-466159665459; xpm=1%2B1654480740%2BWHMuN-dcOBqeI-JqQXna-U~%2B0; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjM1MzEiLCJ0aW1lc3RhbXAiOjE2NTQ0ODA3NDI0NzJ9LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTY1NDQ4MDc0MjQ3MiwiYmFzZSI6Ijk4NTEzIn0sInZhbGlkYXRlS2V5IjoicHJvZDp2MjphYTkyMDVmOS01ZDQ1LTQ5NTEtODI5My0zMGE4ZmRjNDhjZGIifQ%3D%3D; ak_bmsc=5CC4FBD74B08A48FA8FAC168E03C9905~000000000000000000000000000000~YAAQni4gF9n63vOAAQAAYqu8NhBDHmxXL4RRefQNALuxq6Ko/XWCposEIS2Nia5153NuDKk5MBK2F92xH7MW3f56xNajbCvHEowr4PpXDI05zmtDGzTnDjaz1Hpwht44cZhkxpdUxWhWkZqhdRN83el+BEejkhTqAiB8yWt5LbO9pM0JsnhgUlw04PPEZpMv8whXTrrThSjG+dIM0D87rQgMMDzVqLKEzkR43oRem86QiVRh8qWWZyrr2AmPqqAiXLF+Kx5DnolVeZyvG6bTBZsNl4eVUiOehLL/nQGuV2v/9EYf/VXBM091caJkMYz8bNsSSDmK657J5gwmMrOBJD/jHz6hkIxsrXRajtuVHAZkmk5NuiU0BjCjIyDUbj94ggJMe1V4caaczLj09eG9d6uJKQnPi+mTO73OJCdMzkJA9bKeRiR+VsPXLyL5/Sis+IcAi0kgaPV2FtWn3hYEWOqXZeVGjjGoWEVgLcKgbWoidt4Y/JcdgfM=; tb_sw_supported=true; TB_SFOU-100=1; _astc=649ace27ad29ff4f069f5d2bd3a62c0b; wmlh=1f5de094aba24c87662849da8396d7b8998e0fd910800c542f090e6bd150a924; auth=MTAyOTYyMDE4GlnuGnmannbXkE6HlLdYUOkdOGeuqBkzlFH7Mm33QgaJbBqto8IAb7Go6kYuHI1KDzZAQMT%2BmrKJsNE%2By3aVtBLMmuEAyOWlYSVsVDa0DAKO8%2BgWPmwn%2Fyx1o2RajHeU767wuZloTfhm7Wk2KcjygkeeSCv4Chv5IarMOQ7pqjd0GpO9V%2Bts5MrHkEH9Gp%2BBEaiaooIt6%2B5oTRTiPBv144D40Dol74QQOZjFpcghoZ4UMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrveIyvkgZS%2B8el2PKU31L7yFjL40rb%2FLNMR%2FCDuxkoZFedD3gj%2FHiCIKp%2BjexH3pQgCE%2FiQ4rnWvNSxctWODk%2BD%2BFoORq2AyS%2F%2B1UNO0zkVcARNmelvXwreEtYvqQOaMLpE5WBBdZBCyKnCQAR7o6eg%3D; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIzNTMxIiwiZGlzcGxheU5hbWUiOiJMYWNleSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5ODUxNiIsImFkZHJlc3NMaW5lMSI6IjE0MDEgR2FsYXh5IERyIE5lIiwiY2l0eSI6IkxhY2V5Iiwic3RhdGUiOiJXQSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiOTg1MTYtNDc0NiJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6NDcuMDYwNDY1LCJsb25naXR1ZGUiOi0xMjIuNzczODQ0fSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiaHViTm9kZUlkIjoiMzUzMSIsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfSU5TVE9SRSIsIlBJQ0tVUF9DVVJCU0lERSJdfV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6NDcuMDA3OSwibG9uZ2l0dWRlIjotMTIyLjc1MzMsInBvc3RhbENvZGUiOiI5ODUxMyIsImNpdHkiOiJPbHltcGlhIiwic3RhdGUiOiJXQSIsImNvdW50cnlDb2RlIjoiVVNBIiwiZ2lmdEFkZHJlc3MiOmZhbHNlfSwiYXNzb3J0bWVudCI6eyJub2RlSWQiOiIzNTMxIiwiZGlzcGxheU5hbWUiOiJMYWNleSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiI0NzU3IiwiZGlzcGxheU5hbWUiOiJMYWNleSBOZWlnaGJvcmhvb2QgTWFya2V0Iiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijk4NTAzIiwiYWRkcmVzc0xpbmUxIjoiNTExMCBZZWxtIEhpZ2h3YXkiLCJjaXR5IjoiTGFjZXkiLCJzdGF0ZSI6IldBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5ODUwMy0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjo0Ni45OTcyMDYsImxvbmdpdHVkZSI6LTEyMi44MTg3NTd9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjpmYWxzZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiNDc1NyIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NTQ1MDQ4MTUwODIsInZhbGlkYXRlS2V5IjoicHJvZDp2MjphYTkyMDVmOS01ZDQ1LTQ5NTEtODI5My0zMGE4ZmRjNDhjZGIifQ%3D%3D; TS01b0be75=01538efd7cb4fcf86127a4ae973c71254d33df93d33d79fedcf4a3cfd6260e3ecae73b063e1b9489b31719107fe00ae664b6c36b19; _px3=1bda87a022349d17caac3ba2497fffabe44a4e68c4650a1d24113fcf95a6661f:GwS7qF1vzG3JoPoAwYrwMmP8eqNW02x2u272pdjDZ9O0m3wIn9vgztxEKnpt6G8Zf1bokEO3mb0cTJJdMjvg1w==:1000:tOBvDbXQ9zRTEUmJktpI6JYtjixOO2dqS6N2ZEwpLncbvvuS33zQGD0Uqve/qjlgVMCZKXgTNtQEZ3QE1R2XXm5lN5hHcbd/Xp9QpkapLbOcrYA/wTIxyEcjyUtgEASV7uiuxpkCBEIfv7zgWgIftAzGYHXWenZtS8QtLnwK4s3JexaeEV2yWFTr0SizNR5fv4xe6na0G7BX90vHS7QxSQ==; xptwg=2815869025:187F91103D97650:3F98B5F:BFCF9823:D49C1F97:72B416FE:; akavpau_p2=1654484498~id=b261c117fcf4926ce8a1eb00b52ac3fe; bm_sv=EB3E7DC9F25C6272D5DAE6823C2B0442~YAAQhC4gF09t5vWAAQAA8s7sNhDIQe01SFbiHKFlYgqAkQCYlRX1CR4OZ5wELbhO8vM55xSpB1xv9aTH0frDn+72kObB3AeVHe15QB6JEffzbv0Pc4SrWPxypTUaZgAqYcAsWHc05WP21UENvo66F3/7uGRBe60iZH3Y7fukGfnRy1OnCvez09L5MwOAwuHE5PZtRG3Hh52KQ82CcytzFQfi1bmSJ3RaEc9QTDVKqGr+oD+boVkWHOvHd9wuGCRvRy4=~1; ACID=b7468c25-85bc-49cd-95e0-eaa09556d165; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; TS013ed49a=01538efd7ccbe491c1206d0035eb870503d13c5e63d4d4bc3ff1da836db5384f4036ffde1361b022b6a4927c6d263f879b82c9e76f; ak_bmsc=5CC4FBD74B08A48FA8FAC168E03C9905~000000000000000000000000000000~YAAQhy4gF5WHKSWBAQAA7OPwNhBTOLdJQ010pJkGRzuJ+TrKNVSfzjujGBh5dzffXFG4v/xfe6PGAV5TE+adNJUPJM6xLer/1dMcztgEcaQN/R0d4tzcRVqFTeMlfEFUaqcHWACUftc1PQsFaOIo5mra1DGCpHyCUUPF/+dY7rRnoCDk6rBqy7x3QFjmC+73/41pm+zHoMNCZqqEpjlnSPqhxSoQWE0EuhDh5F26iRj9iaEE+lmoHrCtP4Tj1zt384xr3JVHla8Sve/tYmDYHJyGe9baphiNNU4LUOHWEKeyy8oGHklTNBms3g4qqm7qy4ph/HMHZrHr1VwSzFQLOPX9WXy0CvvHAOLc1HhvEedpwu9SfNgDTmfKzyR0415S/R40lMylrzUnI/0uZv4zVWqHo8+Tk7vYHaEZQ+IzLk0LSDwsPDkOtNDB8tNdsuT650onR6fpL9A/t8eAiBqVxsocFq/+7R1pyHQdDdjTFHCqh0U23r2vTIXmyirN3mQ=; assortmentStoreId=3531; auth=MTAyOTYyMDE491W2ipO%2Ba1alPAYvzCrqoTONC6QI1kOkYlQ06gEDHmBf4HGA3hRFG496QjQWWIMPdhp51jIm0V3ZBZ%2Bv8r0925CMPxTlYCaUAOsLY1UEl2yoPk8bL%2FZQHpsivZd3nasI767wuZloTfhm7Wk2Kcjygv3M5Jnvc7ePkiG6%2BkglNAB6h13H8cNjQ5TzDIrOfaKk4hY%2BL1SIV9nEI4SFvB4BtQeN%2FXQKYVcEX9AuxcaFUNIUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrq00V18pk9WmbUCZ%2B94IdLPquRpEIt6lgeFA4hYs3U2%2BCg5J19yw%2FFo7wNuD%2BqWFp%2B%2Bnys96pSxF7vu67SkRKBb%2BFoORq2AyS%2F%2B1UNO0zkVcWNbGXx7XPLzMQeG365KgtCQzX7MAlLBJXxL%2Bwi6fx6Y%3D; bm_mi=97BD375D2FD687AFD543DD51D35CE67D~YAAQhy4gF8o0KSWBAQAA9lfsNhDyMhjH/CPv1PzIYojqktLTz4yr4TlDMXJWfXXEe0/Adu52VLYptdOFjwjqMGcYG6QJGaZhmVbNvItxq4k7Oha+ImTrCAyIkX9oWEtGFVVinm71aNJK9YpbuFOGQUa24Wr/tw5EyntI4QWtKRhSefmejzt/RZjB+8DTElxcWA7okHzVS9mm8ZAkQvQQT/kdlxWwWwSri0A5Ki/rSoPgTHEMMckmY/1zsxKwHamgNeJZXSN+9m+TJ7KdvSos9gSMMCa85szMo26YfvbLpcjwoNYGlSTp6UoWVIWSKA==~1; bm_sv=EB3E7DC9F25C6272D5DAE6823C2B0442~YAAQhy4gF5aHKSWBAQAA7OPwNhAMVsF3zN+OIH+B6VrQjYzKkBRUkCE9Zv9FvG2tIxBz5BIneuNkq58Z34CIgcMFI1SEEZnGMBG+NNnggKjhGDaduTsUuquBOBWe7tfrQM9rCsyP9I5nb7nL/pRxT5nGgJaGOtTIbOP7GKYRNVa6+Hm/n+IN5C9R8UP505y1l8rZwKdKMPJRszQzdijzzsBMGmIcMdLOqzLOf7004kxArSmUihNVwfaHP1ZmBAwd+/o=~1; bstc=WHMuN-dcOBqeI-JqQXna-U; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1654484165000@firstcreate:1649092530820"; exp-ck=09BXG20t4gT11jR7v16Yrc-18wp7a2Dmnts3Pgtnl1R-V1g1ccDGr1eJ9VH2eXnIH1gVG-b1gynZP2hGNr-1obzLE1; hasACID=true; hasLocData=1; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIzNTMxIiwiZGlzcGxheU5hbWUiOiJMYWNleSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5ODUxNiIsImFkZHJlc3NMaW5lMSI6IjE0MDEgR2FsYXh5IERyIE5lIiwiY2l0eSI6IkxhY2V5Iiwic3RhdGUiOiJXQSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiOTg1MTYtNDc0NiJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6NDcuMDYwNDY1LCJsb25naXR1ZGUiOi0xMjIuNzczODQ0fSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiaHViTm9kZUlkIjoiMzUzMSIsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfSU5TVE9SRSIsIlBJQ0tVUF9DVVJCU0lERSJdfV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6NDcuMDA3OSwibG9uZ2l0dWRlIjotMTIyLjc1MzMsInBvc3RhbENvZGUiOiI5ODUxMyIsImNpdHkiOiJPbHltcGlhIiwic3RhdGUiOiJXQSIsImNvdW50cnlDb2RlIjoiVVNBIiwiZ2lmdEFkZHJlc3MiOmZhbHNlfSwiYXNzb3J0bWVudCI6eyJub2RlSWQiOiIzNTMxIiwiZGlzcGxheU5hbWUiOiJMYWNleSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiI0NzU3IiwiZGlzcGxheU5hbWUiOiJMYWNleSBOZWlnaGJvcmhvb2QgTWFya2V0Iiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijk4NTAzIiwiYWRkcmVzc0xpbmUxIjoiNTExMCBZZWxtIEhpZ2h3YXkiLCJjaXR5IjoiTGFjZXkiLCJzdGF0ZSI6IldBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5ODUwMy0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjo0Ni45OTcyMDYsImxvbmdpdHVkZSI6LTEyMi44MTg3NTd9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjpmYWxzZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiNDc1NyIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NTQ1MDUzMDg3NjEsInZhbGlkYXRlS2V5IjoicHJvZDp2MjpiNzQ2OGMyNS04NWJjLTQ5Y2QtOTVlMC1lYWEwOTU1NmQxNjUifQ%3D%3D; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjM1MzEiLCJ0aW1lc3RhbXAiOjE2NTQ0ODE4MDU2NDd9LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTY1NDQ4MTgwNTY0NywiYmFzZSI6Ijk4NTEzIn0sInZhbGlkYXRlS2V5IjoicHJvZDp2MjpiNzQ2OGMyNS04NWJjLTQ5Y2QtOTVlMC1lYWEwOTU1NmQxNjUifQ%3D%3D; mobileweb=0; vtc=WHMuN-dcOBqeI-JqQXna-U; xpa=-wnVY|09BXG|0t4gT|1jR7v|6Yrc-|8wp7a|Dmnts|LTD5Y|Pgtnl|QnZNm|R-V1g|Umo04|bupnU|ccDGr|duBe9|eJ9VH|eXnIH|gVG-b|gynZP|hGNr-|jf5Jq|obzLE|opVBu|sGDe9|srerY|viJr2; xpm=7%2B1654483700%2BUbKxclxS5rvBE8ylsIrSqA~%2B0; xptwg=257500375:1A76C5602903540:44B3011:7A093066:B7AE2C73:70245CF:; TS01b0be75=01538efd7ccf13ca32e63eefa4f7c771e7d252fdba73268e96ce56fc63b098f320ed82ade7b5e513d4c2d96512d27d88cc498073c5; akavpau_p2=1654484765~id=c4bc31a89365ef60aa26925601fd9780',
  'device_profile_ref_id': 'u868JtPnnUUUpLjYzyhfNqzjk7QXoYCke3Z4',
  'origin': 'https://www.walmart.com',
  'referer': 'https://www.walmart.com/browse/food/milk/976759_9176907_4405816?page=6&affinityOve58ride=default&affinityOverride=default',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': 'GqcssZUI0stVTjyr8_LpYU04_1_z4v3CrqDf',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
  'wm_mp': 'true',
  'wm_page_url': 'https://www.walmart.com/browse/food/milk/976759_9176907_4405816?page=6&affinityOve58ride=default&affinityOverride=default',
  'wm_qos.correlation_id': 'GqcssZUI0stVTjyr8_LpYU04_1_z4v3CrqDf',
  'x-apollo-operation-name': 'Browse',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-US',
  'x-o-ccm': 'server',
  'x-o-correlation-id': 'GqcssZUI0stVTjyr8_LpYU04_1_z4v3CrqDf',
  'x-o-gql-query': 'query Browse',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-496-dfe8cb',
  'x-o-segment': 'oaoh'
}

def WalmartRequest(updateURL, insertHeaders, insertPayload, tableName, categoryName): 
  for page in range(1, 100, 1):
    test = updateURL.replace("page=1", "page=" + str(page))
    newURL = f"{test}"
    r = requests.post(newURL, headers=insertHeaders, data=insertPayload)
    data = json.loads(r.text)
    if(r.ok == True):
        newData = data
        time.sleep(2)
        break
        print(f'Getting page {page} of ' + categoryName + ' ' + tableName, 'waiting..')
    else:
      break
  
  # filteredData = []
  # # Filtering out duplicate data from our request by going through each object and seeing if its already in our filtered data object.
  # for x in newData:
  #   if x not in filteredData: 
  #     filteredData.append(x)
  prods = pd.DataFrame([])
  prods = prods.from_records(pd.json_normalize(newData)) 
  #prods = prods.drop(columns=['sellByWeight','aisleName', 'prop65WarningIconRequired', 'departmentName', 'pid', 'aisleId', 'upc', 'restrictedValue', 'displayType', 'averageWeight', 'salesRank', 'id', 'featured', 'inventoryAvailable', 'pastPurchased', 'isArProduct', 'displayUnitQuantityText', 'promoEndDate', 'isMtoProduct', 'displayEstimateText', 'channelEligibility.delivery', 'channelEligibility.inStore', 'channelEligibility.pickUp', 'channelInventory.delivery', 'channelInventory.pickup', 'channelInventory.instore', 'preparationTime', 'unitQuantity', 'basePrice'], axis=1)
  prods.to_csv('Walmart' + str(categoryName) + '.csv')


WalmartRequest(url, headers,  payload, "Milk", "Dairy")
