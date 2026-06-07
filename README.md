# WaxCast
An ML-driven Nordic ski wax recommendation engine that predicts snow states by modeling thermodynamic history from local weather APIs. Built with Go, Python (XGBoost), and React.

Traditional cross-country ski wax applications rely on rigid, manual lookup tables. To get an accurate recommendation, existing software forces the user to manually input hyper-specific environmental variables such as snow crystal geometry (e.g., new vs. transformed vs. corn snow) and exact snow moisture content. The reality is that 95% of casual and regional racers do not possess the domain expertise or specialized tools to measure these variables at the trailhead. As a result, users guess incorrectly, leading to sub-optimal ski glide, poor kick traction, and a broken user experience.

Instead of asking the user to analyze snow crystals, WaxCast treats snow structure as a deterministic function of recent thermodynamic history. Instead of relying on human guesswork, an XGBoost classifier uses this multi-dimensional temporal data as a proxy to infer the underlying physical state of the snow pack automatically.

Building this application required solving several non-trivial software engineering and mathematical constraints:

Weather APIs provide messy, fragmented historical timelines. The backend (built in Go/Python) implements robust data-cleaning pipelines to handle missing data fields, normalize localized time zones, and compute feature vectors (like rate of temperature change) on the fly.

Following recent international bans on fluorinated chemical waxes, the competitive skiing landscape shifted overnight. This project maps an open-source, multi-brand catalog of modern non-fluoro hydrocarbon and liquid waxes, dynamically matching them to predicted snow states.

By decoupling the heavy ML inference pipeline into a lightweight, containerized microservice, the front-end React application delivers responsive, interactive, map-based wax forecasts in milliseconds.
