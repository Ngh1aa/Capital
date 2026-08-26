# Google Static Maps setup for Capital Place

The Location page is ready for the **Google Static Maps Hybrid** background. The implementation keeps POIs as local HTML/CSS buttons and calculates their positions from latitude/longitude using the same Web Mercator projection as the map viewport.

## Add the public browser key

1. In [Google Cloud Console](https://console.cloud.google.com/), create or select a project, enable **Maps Static API**, attach billing, and create an API key.
2. Restrict the key by **HTTP referrers**. Add `https://ngh1aa.github.io/Capital/*` and, if a custom domain will be added later, its equivalent path.
3. Under API restrictions, allow only **Maps Static API**.
4. Open `assets/location-map-config.js` and set `apiKey` to the restricted browser key. The key is public by design because the site is GitHub Pages; the HTTP referrer and API restrictions are the security boundary.
5. Do not use a server key or unrestricted key in this file.

The request uses `center=21.03180,105.81385`, `zoom=15`, `size=640x480`, `scale=2`, `maptype=hybrid`, `language=en`, `region=VN`, and `format=jpg`. If the key is empty or the request fails, the page keeps the verified local road map as a graceful fallback and shows a small configuration status inside the map.

## Sources

Google documents that Static Maps returns an image through an HTTP URL, requires an API key and billing, supports `size`, `scale`, `maptype=hybrid`, `language` and `region`, and recommends HTTPS for web pages. See [Maps Static API — Get Started](https://developers.google.com/maps/documentation/maps-static/start) and [Set up the Maps Static API](https://developers.google.com/maps/documentation/maps-static/get-api-key).
