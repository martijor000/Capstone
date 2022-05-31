from WalmartReq import WalmartRequest
import requests
import json
import pandas as pd
import time
from sqlalchemy import create_engine, false

url = "https://www.walmart.com/orchestra/home/graphql/browse?affinityOverride=default&page=1&prg=desktop&catId=976759_9176907_4405816&sort=best_match&ps=40&searchArgs.cat_id=976759_9176907_4405816&searchArgs.prg=desktop&fetchMarquee=true&fetchSkyline=true&fetchSbaTop=false&enablePortableFacets=true&tenant=WM_GLASS"

payload = json.dumps({
  "query": "query Browse( $query:String $page:Int $prg:Prg! $facet:String $sort:Sort $catId:String! $max_price:String $min_price:String $module_search:String $affinityOverride:AffinityOverride $ps:Int $ptss:String $beShelfId:String $fitmentFieldParams:JSON ={}$fitmentSearchParams:JSON ={}$rawFacet:String $seoPath:String $trsp:String $fetchMarquee:Boolean! $fetchSkyline:Boolean! $additionalQueryParams:JSON ={}$enablePortableFacets:Boolean = false $tenant:String! ){search( query:$query page:$page prg:$prg facet:$facet sort:$sort cat_id:$catId max_price:$max_price min_price:$min_price module_search:$module_search affinityOverride:$affinityOverride additionalQueryParams:$additionalQueryParams ps:$ps ptss:$ptss trsp:$trsp _be_shelf_id:$beShelfId ){query searchResult{...BrowseResultFragment}}contentLayout( channel:\"WWW\" pageType:\"BrowsePage\" tenant:$tenant version:\"v1\" searchArgs:{query:$query cat_id:$catId _be_shelf_id:$beShelfId prg:$prg}){modules{...ModuleFragment configs{...on EnricherModuleConfigsV1{zoneV1}__typename...on _TempoWM_GLASSWWWSearchSortFilterModuleConfigs{facetsV1 @skip(if:$enablePortableFacets){...FacetFragment}topNavFacets @include(if:$enablePortableFacets){...FacetFragment}allSortAndFilterFacets @include(if:$enablePortableFacets){...FacetFragment}}...on TempoWM_GLASSWWWPillsModuleConfigs{moduleSource pillsV2{...PillsModuleFragment}}...TileTakeOverProductFragment...on TempoWM_GLASSWWWSearchFitmentModuleConfigs{fitments( fitmentSearchParams:$fitmentSearchParams fitmentFieldParams:$fitmentFieldParams ){...FitmentFragment sisFitmentResponse{...BrowseResultFragment}}}...on TempoWM_GLASSWWWStoreSelectionHeaderConfigs{fulfillmentMethodLabel storeDislayName}...on TempoWM_GLASSWWWSponsoredProductCarouselConfigs{_rawConfigs}...PopularInModuleFragment...CopyBlockModuleFragment...BannerModuleFragment...HeroPOVModuleFragment...InlineSearchModuleFragment...MarqueeDisplayAdConfigsFragment @include(if:$fetchMarquee)...SkylineDisplayAdConfigsFragment @include(if:$fetchSkyline)...HorizontalChipModuleConfigsFragment}}...LayoutFragment pageMetadata{location{pickupStore deliveryStore intent postalCode stateOrProvinceCode city storeId accessPointId accessType}pageContext}}seoBrowseMetaData( id:$catId facets:$rawFacet path:$seoPath facet_query_param:$facet _be_shelf_id:$beShelfId ){metaTitle metaDesc metaCanon h1}}fragment BrowseResultFragment on SearchInterface{title aggregatedCount...BreadCrumbFragment...ShelfDataFragment...DebugFragment...ItemStacksFragment...PageMetaDataFragment...PaginationFragment...RequestContextFragment...ErrorResponse modules{facetsV1 @skip(if:$enablePortableFacets){...FacetFragment}topNavFacets @include(if:$enablePortableFacets){...FacetFragment}allSortAndFilterFacets @include(if:$enablePortableFacets){...FacetFragment}pills{...PillsModuleFragment}}}fragment ModuleFragment on TempoModule{name version type moduleId schedule{priority}matchedTrigger{zone}}fragment LayoutFragment on ContentLayout{layouts{id layout}}fragment BreadCrumbFragment on SearchInterface{breadCrumb{id name url}}fragment ShelfDataFragment on SearchInterface{shelfData{shelfName shelfId}}fragment DebugFragment on SearchInterface{debug{sisUrl adsUrl}}fragment ItemStacksFragment on SearchInterface{itemStacks{displayMessage meta{adsBeacon{adUuid moduleInfo max_ads}query stackId stackType title layoutEnum totalItemCount totalItemCountDisplay viewAllParams{query cat_id sort facet affinityOverride recall_set min_price max_price}}itemsV2{...ItemFragment...InGridMarqueeAdFragment...TileTakeOverTileFragment}}}fragment ItemFragment on Product{__typename id usItemId fitmentLabel name checkStoreAvailabilityATC seeShippingEligibility brand type shortDescription imageInfo{...ProductImageInfoFragment}canonicalUrl externalInfo{url}itemType category{path{name url}}badges{flags{...on BaseBadge{key text type id}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{...on BaseBadge{key text type}}}classType averageRating numberOfReviews esrb mediaRating salesUnitType sellerId sellerName hasSellerBadge availabilityStatusV2{display value}groupMetaData{groupType groupSubType numberOfComponents groupComponents{quantity offerId componentType productDisplayName}}productLocation{displayValue aisle{zone aisle}}fulfillmentSpeed offerId preOrder{...PreorderFragment}priceInfo{...ProductPriceInfoFragment}variantCriteria{...VariantCriteriaFragment}snapEligible fulfillmentBadge fulfillmentTitle fulfillmentType brand manufacturerName showAtc sponsoredProduct{spQs clickBeacon spTags}showOptions showBuyNow rewards{eligible state minQuantity rewardAmt promotionId selectionToken cbOffer term expiry description}}fragment ProductImageInfoFragment on ProductImageInfo{thumbnailUrl}fragment ProductPriceInfoFragment on ProductPriceInfo{priceRange{minPrice maxPrice}currentPrice{...ProductPriceFragment}wasPrice{...ProductPriceFragment}unitPrice{...ProductPriceFragment}listPrice{...ProductPriceFragment}shipPrice{...ProductPriceFragment}subscriptionPrice{priceString subscriptionString}priceDisplayCodes{priceDisplayCondition finalCostByWeight submapType}}fragment PreorderFragment on PreOrder{isPreOrder preOrderMessage preOrderStreetDateMessage}fragment ProductPriceFragment on ProductPrice{price priceString}fragment VariantCriteriaFragment on VariantCriterion{name type id isVariantTypeSwatch variantList{id images name rank swatchImageUrl availabilityStatus products selectedProduct{canonicalUrl usItemId}}}fragment InGridMarqueeAdFragment on MarqueePlaceholder{__typename type moduleLocation lazy}fragment TileTakeOverTileFragment on TileTakeOverProductPlaceholder{__typename type tileTakeOverTile{span title subtitle image{src alt}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title}ctaType ctaTextColor}}}fragment PageMetaDataFragment on SearchInterface{pageMetadata{storeSelectionHeader{fulfillmentMethodLabel storeDislayName}title canonical description location{addressId}}}fragment PaginationFragment on SearchInterface{paginationV2{maxPage pageProperties}}fragment RequestContextFragment on SearchInterface{requestContext{vertical isFitmentFilterQueryApplied searchMatchType categories{id name}}}fragment ErrorResponse on SearchInterface{errorResponse{correlationId source errorCodes errors{errorType statusCode statusMsg source}}}fragment PillsModuleFragment on PillsSearchInterface{title url image:imageV1{src alt}}fragment BannerModuleFragment on TempoWM_GLASSWWWSearchBannerConfigs{moduleType viewConfig{title image imageAlt displayName description url urlAlt appStoreLink appStoreLinkAlt playStoreLink playStoreLinkAlt}}fragment PopularInModuleFragment on TempoWM_GLASSWWWPopularInBrowseConfigs{seoBrowseRelmData(id:$catId){relm{id name url}}}fragment CopyBlockModuleFragment on TempoWM_GLASSWWWCopyBlockConfigs{copyBlock(id:$catId){cwc}}fragment FacetFragment on Facet{title name type layout min max selectedMin selectedMax unboundedMax stepSize isSelected values{id name description type itemCount isSelected baseSeoURL}}fragment FitmentFragment on Fitments{partTypeIDs result{status formId position quantityTitle extendedAttributes{...FitmentFieldFragment}labels{...LabelFragment}resultSubTitle notes suggestions{...FitmentSuggestionFragment}}labels{...LabelFragment}savedVehicle{vehicleYear{...VehicleFieldFragment}vehicleMake{...VehicleFieldFragment}vehicleModel{...VehicleFieldFragment}additionalAttributes{...VehicleFieldFragment}}fitmentFields{...VehicleFieldFragment}fitmentForms{id fields{...FitmentFieldFragment}title labels{...LabelFragment}}}fragment LabelFragment on FitmentLabels{ctas{...FitmentLabelEntityFragment}messages{...FitmentLabelEntityFragment}links{...FitmentLabelEntityFragment}images{...FitmentLabelEntityFragment}}fragment FitmentLabelEntityFragment on FitmentLabelEntity{id label}fragment VehicleFieldFragment on FitmentVehicleField{id label value}fragment FitmentFieldFragment on FitmentField{id displayName value extended data{value label}dependsOn}fragment FitmentSuggestionFragment on FitmentSuggestion{id position loadIndex speedRating searchQueryParam labels{...LabelFragment}cat_id fitmentSuggestionParams{id value}}fragment HeroPOVModuleFragment on TempoWM_GLASSWWWHeroPovConfigsV1{povCards{card{povStyle image{mobileImage{...TempoCommonImageFragment}desktopImage{...TempoCommonImageFragment}}heading{text textColor textSize}subheading{text textColor}detailsView{backgroundColor isTransparent}ctaButton{button{linkText clickThrough{value}uid}}logo{...TempoCommonImageFragment}links{link{linkText}}}}}fragment TempoCommonImageFragment on TempoCommonImage{src alt assetId uid clickThrough{value}}fragment InlineSearchModuleFragment on TempoWM_GLASSWWWInlineSearchConfigs{headingText placeholderText}fragment MarqueeDisplayAdConfigsFragment on TempoWM_GLASSWWWMarqueeDisplayAdConfigs{_rawConfigs ad{...DisplayAdFragment}}fragment DisplayAdFragment on Ad{...AdFragment adContent{type data{__typename...AdDataDisplayAdFragment}}}fragment AdFragment on Ad{status moduleType platform pageId pageType storeId stateCode zipCode pageContext moduleConfigs adsContext adRequestComposite}fragment AdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment SkylineDisplayAdConfigsFragment on TempoWM_GLASSWWWSkylineDisplayAdConfigs{_rawConfigs ad{...SkylineDisplayAdFragment}}fragment SkylineDisplayAdFragment on Ad{...SkylineAdFragment adContent{type data{__typename...SkylineAdDataDisplayAdFragment}}}fragment SkylineAdFragment on Ad{status moduleType platform pageId pageType storeId stateCode zipCode pageContext moduleConfigs adsContext adRequestComposite}fragment SkylineAdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment HorizontalChipModuleConfigsFragment on TempoWM_GLASSWWWHorizontalChipModuleConfigs{chipModuleSource:moduleSource chipModule{title url{linkText title clickThrough{type value}}}chipModuleWithImages{title url{linkText title clickThrough{type value}}image{alt clickThrough{type value}height src title width}}}fragment TileTakeOverProductFragment on TempoWM_GLASSWWWTileTakeOverProductConfigs{TileTakeOverProductDetails{span dwebPosition mwebPosition title subtitle image{src alt}logoImage{src alt}backgroundColor titleTextColor subtitleTextColor tileCta{ctaLink{clickThrough{value}linkText title}ctaType ctaTextColor}}}",
  "variables": {
    "id": "",
    "affinityOverride": "default",
    "dealsId": "",
    "query": "",
    "page": 3,
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
      "page": 3,
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
  'cookie': 'QuantumMetricUserID=1c34634a43bc06585c086015cf1116ee; auth=MTAyOTYyMDE4bTHp%2Fkg13U1w8cm1Axs%2BtC5DSLFtko7xayvxDGM5PU2hIS6u7I96rBu%2FsNIifHxkeAyjhX9ZyjnSnGHzqEcFlH%2Fo2ib0YIk7vLSEWpdiYKfKe8P%2FwlmZzYrUaq3BrPBL767wuZloTfhm7Wk2Kcjygi5k0VvBM%2FJjwcKWWhCnBS96QzUZdpxoR2i%2FOg3bCG6eyzuHZCQMPnQ1VOXVovuWz9sPt%2Bzr5C1iDsQrsCFo5UQUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKroVQU%2B2XgiMMD37W30vcxsi9xCeKWAtDNCuElhvSzwtlmYq9aEQPhKEvwXMxWkDsSxg%2FI5dzKjM9UVSIz9zuv0GajMOOTsVYgwbMpAUR0Ntjf8ULQwkuPUKiQHbc5skLfiQzX7MAlLBJXxL%2Bwi6fx6Y%3D; ACID=0ff0fa35-cb2e-4add-8bc5-e01df97cc1c2; hasACID=true; assortmentStoreId=3531; hasLocData=1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; vtc=UbKxclxS5rvBE8ylsIrSqA; bstc=UbKxclxS5rvBE8ylsIrSqA; mobileweb=0; xpa=0t4gT|1jR7v|6Yrc-|6sE52|6uVhz|8wp7a|DY63U|HF8Yi|LTD5Y|OQQMu|QnZNm|V7I-O|VxKe2|ccDGr|duBe9|eJ9VH|eXnIH|gVG-b|gynZP|iUsRT|jf5Jq|lUKHC|mD451|mH3sb|obzLE|srerY|viJr2; exp-ck=0t4gT11jR7v16Yrc-16uVhz28wp7a1DY63U1OQQMu1VxKe21ccDGr1eJ9VH2eXnIH1gVG-b1gynZP2iUsRT1lUKHC1mD4511obzLE1; _cvftc=rest; TS013ed49a=01538efd7c0d8221eb26ca790dbce6adb98ac770d22baa715db57471c77b2b86990ae8dca9e4c394d35d793b0ce01c5cb183f47680; TBV=7; dimensionData=961; adblocked=false; xpm=1%2B1653887096%2BUbKxclxS5rvBE8ylsIrSqA~%2B0; pxcts=0da170e2-dfd6-11ec-80ea-6169624d6e49; _pxvid=0da169d1-dfd6-11ec-80ea-6169624d6e49; ak_bmsc=A5B0686B4BD3B9D8543F0CCF5CFB1D93~000000000000000000000000000000~YAAQTS4gFzGiqPCAAQAAoGBaEw+CF6j7clBm5dtHJfbBlSUJ/Rvp/brbAUfgdrL7vSKSR1stSfB5N+g0Q4uhBZhE4qa/jIiZAe8ru7Q+U5iD+A4S24WIhcnRqWi0iDdCKaGAQnJeTrLpESkTll75aAFGEVirlZgTX7vCKf6yKZ933T+zzDLKgYIlmvy1TdQygEi4D/ReaY8+zrTsCr0fir0YVBL5Fn2C2L0znRqxiubioe7vovDjQ9S/rEKuHBbzaZ0d6YL5vsz9pXV3rtJhfKIWb88BADCpgxVwhpc84NzgB7d7XGr+b/GNCjYFvrren2V/qMW+aAnuB4th11jWiuouFKQjltTf88liSrGlN/YfSvzX+Wma3zKIamT/lqvDvxXHg2d0Pnl9CtY95CZfvGrv5+NePJ+g73xrzTZP6fTXuz+obQkP8St1Jw2OL9faRj7TjHSteG/pGjjVBscyouR6iDiTyMuA1ufemMrMbNAFc3FYhhCFUQg=; tb_sw_supported=true; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIzNTMxIiwiZGlzcGxheU5hbWUiOiJMYWNleSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5ODUxNiIsImFkZHJlc3NMaW5lMSI6IjE0MDEgR2FsYXh5IERyIE5lIiwiY2l0eSI6IkxhY2V5Iiwic3RhdGUiOiJXQSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiOTg1MTYtNDc0NiJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6NDcuMDYwNDY1LCJsb25naXR1ZGUiOi0xMjIuNzczODQ0fSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiaHViTm9kZUlkIjoiMzUzMSIsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJCQUtFUllfUElDS1VQIiwiUElDS1VQX0lOU1RPUkUiLCJQSUNLVVBfQ1VSQlNJREUiLCJQSUNLVVBfU1BFQ0lBTF9FVkVOVCJdfV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6NDcuMDA3OSwibG9uZ2l0dWRlIjotMTIyLjc1MzMsInBvc3RhbENvZGUiOiI5ODUxMyIsImNpdHkiOiJPbHltcGlhIiwic3RhdGUiOiJXQSIsImNvdW50cnlDb2RlIjoiVVNBIiwiZ2lmdEFkZHJlc3MiOmZhbHNlfSwiYXNzb3J0bWVudCI6eyJub2RlSWQiOiIzNTMxIiwiZGlzcGxheU5hbWUiOiJMYWNleSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiI0NzU3IiwiZGlzcGxheU5hbWUiOiJMYWNleSBOZWlnaGJvcmhvb2QgTWFya2V0Iiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijk4NTAzIiwiYWRkcmVzc0xpbmUxIjoiNTExMCBZZWxtIEhpZ2h3YXkiLCJjaXR5IjoiTGFjZXkiLCJzdGF0ZSI6IldBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5ODUwMy0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjo0Ni45OTcyMDYsImxvbmdpdHVkZSI6LTEyMi44MTg3NTd9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjpmYWxzZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiNDc1NyIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NTM5MDg2OTkxNDIsInZhbGlkYXRlS2V5IjoicHJvZDp2MjowZmYwZmEzNS1jYjJlLTRhZGQtOGJjNS1lMDFkZjk3Y2MxYzIifQ%3D%3D; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjM1MzEiLCJ0aW1lc3RhbXAiOjE2NTM4ODcwOTkxMzJ9LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTY1Mzg4NzA5OTEzMiwiYmFzZSI6Ijk4NTEzIn0sInZhbGlkYXRlS2V5IjoicHJvZDp2MjowZmYwZmEzNS1jYjJlLTRhZGQtOGJjNS1lMDFkZjk3Y2MxYzIifQ%3D%3D; TB_SFOU-100=1; _astc=649ace27ad29ff4f069f5d2bd3a62c0b; wmlh=1f5de094aba24c87662849da8396d7b8998e0fd910800c542f090e6bd150a924; TS01b0be75=01538efd7ce0c1190190678e35417bcee9b288545a36c4912fd9c2cd5a677641ff58e3912dfce343587b29c72fa3392eacf989b206; _px3=4c5b5aa81530e51c5d01cbebffdf23759b16116f887ebab62bbe3e29b728e11f:ue8ehPbRn024ufA2eorOmufohNyt98cxy+Rt/9p05dHApiR1MoCke78G6dtB7rZiCIxbRDkvXwmPc3S0qcrsnw==:1000:XOFJ0f0UOK03Qft4C9UQaZ+unUr/mPd2qgfv95RwRjapOB9GnIII5JLqz9/pjbKI7X2aLaw+NJ7ukZ6Dr48DNa5/aqq9bg3YzZj7mIm91cLU2gExIsUKkUauD+EYg8htsyWa4GEgmgqXE02PgHUYa+VWCF1RXHCSJloeQ1QeHK/s+xH2gbbdwDz2XtrhnK3YCH7jovbQ6qEkV9YnidOeGA==; xptwg=2829246043:18AA541CD5F4A70:400DA14:97B1DC38:E8EC2407:F0A4D678:; akavpau_p2=1653888075~id=637fd54debb76864e5b4c941d7f8b800; bm_sv=12E7D1376CAF40139DB56AFB88F89581~YAAQbi4gF0jrQPKAAQAAQR5gEw977c3oOTZ5QogVfog1xiN0nu3hxiNnyyl/NgG796eRhwMX5RsY27j+nKZ2+AcqVKINOG8cg++aq/Xe34vEnfBfAM7SCDC424rZck71eu8vZIZZy24YGDPiuqNiON2MqjoPmYqtdNPQMb75rrAPxjNqdRFTw2JNT/4ayzmNjQoAEMsIktHYCHCKSpySn3ncb/DkG0aRg6UKTRQnp5Y26Bq6MGakqlP3u+MXkoCepAs=~1; ACID=b7468c25-85bc-49cd-95e0-eaa09556d165; TS013ed49a=01538efd7c0d8221eb26ca790dbce6adb98ac770d22baa715db57471c77b2b86990ae8dca9e4c394d35d793b0ce01c5cb183f47680; bm_sv=12E7D1376CAF40139DB56AFB88F89581~YAAQjC4gF1NAXt+AAQAAuxViEw/m7gXm45Jyemkw/4kM1vJLjrWL+ZqyGKsusMlLxcjh4FUs8IFy1Kd3YDt0GIHEZVQXPFtW9Ylrb+A+vsYN1VaS7xdtpdddNoDZsdZK47+IvrsMkUkkuPxfEfv0ADKGiUAW2NGVhXXS92wZMbYk0g/NxPs1aqSOUvdN7pHRCKXXJRa+di2qW7mJubRLm6Q6rOwO3tREhZtblJhdBktJ2U4zMptCorIviZonpSRJSoo=~1; bstc=UbKxclxS5rvBE8ylsIrSqA; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1653887604000@firstcreate:1649092530820"; exp-ck=0t4gT11jR7v16Yrc-16uVhz28wp7a1DY63U1OQQMu1VxKe21ccDGr1eJ9VH2eXnIH1gVG-b1gynZP2iUsRT1lUKHC1mD4511obzLE1; hasACID=true; mobileweb=0; vtc=UbKxclxS5rvBE8ylsIrSqA; xpa=0t4gT|1jR7v|6Yrc-|6sE52|6uVhz|8wp7a|DY63U|HF8Yi|LTD5Y|OQQMu|QnZNm|V7I-O|VxKe2|ccDGr|duBe9|eJ9VH|eXnIH|gVG-b|gynZP|iUsRT|jf5Jq|lUKHC|mD451|mH3sb|obzLE|srerY|viJr2; xpm=1%2B1653887096%2BUbKxclxS5rvBE8ylsIrSqA~%2B0; xptwg=3119289776:3D909C4B6B1970:9FE09A:4D45BEAE:1236A02B:233EE9ED:; TS01b0be75=01538efd7ce0c1190190678e35417bcee9b288545a36c4912fd9c2cd5a677641ff58e3912dfce343587b29c72fa3392eacf989b206; akavpau_p2=1653888204~id=3e8993839d1ffc1d4f3c732c215c68c6',
  'device_profile_ref_id': '-uyAOUBRfyDA5HlHXMY5esP2-TT0Ovs0scTK',
  'origin': 'https://www.walmart.com',
  'referer': 'https://www.walmart.com/browse/dairy-eggs/milk/976759_9176907_4405816?page=3&affinityOverride=default',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': 'EYeUAqeWlxmMnT88e2zq_eDDTaPjax9a-9ru',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
  'wm_mp': 'true',
  'wm_page_url': 'https://www.walmart.com/browse/dairy-eggs/milk/976759_9176907_4405816?page=3&affinityOverride=default',
  'wm_qos.correlation_id': 'EYeUAqeWlxmMnT88e2zq_eDDTaPjax9a-9ru',
  'x-apollo-operation-name': 'Browse',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-US',
  'x-o-ccm': 'server',
  'x-o-correlation-id': 'EYeUAqeWlxmMnT88e2zq_eDDTaPjax9a-9ru',
  'x-o-gql-query': 'query Browse',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-496-ab9775',
  'x-o-segment': 'oaoh'
}

WalmartRequest(url, headers,  payload, "Milk", "Dairy")

def WalmartRequest(updateURL, insertHeaders, insertPayload, tableName, categoryName): 
  for page in range(1, 100, 1):
    test = updateURL.replace("page=1", "page=" + str(page))
    newURL = f"{test}"
    r = requests.get(newURL, headers=insertHeaders, data=insertPayload)
    data = json.loads(r.text)
    if(r.ok == false):
        newData = data
        time.sleep(3)
        print(f'Getting row {page} of ' + categoryName + ' ' + tableName, 'waiting..')
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
