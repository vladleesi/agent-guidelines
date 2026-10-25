# Web frontend

- Use semantic HTML and native controls before recreating browser behavior. Provide
  accessible names, visible focus, keyboard operation, meaningful heading order,
  and feedback for loading, empty, invalid, and failed states.
- Build responsive layouts around available space and content. Check text zoom,
  contrast, reduced motion, and relevant themes/input methods. Preserve essential
  content and links without JavaScript when the product supports progressive enhancement.
- Reuse design tokens for colors, typography, and spacing. Keep theme-dependent
  visuals consistent across components and states.
- Clean up listeners, observers, timers, and obsolete requests. Avoid duplicate
  subscriptions and stale responses overwriting newer state; handle unavailable
  storage and network failures without breaking unrelated interactions.
- Preserve browser history, reloadable deep links, and URL/base-path behavior.
  Treat the URL as part of the public contract and avoid in-memory-only navigation
  state for information needed after reload.
- Measure production output before optimizing. Reserve media dimensions, size and
  compress assets appropriately, defer noncritical work, and avoid speculative
  preloading or caching. Match cache policy to whether asset URLs identify content.
- For public indexable pages, keep titles, descriptions, canonicals, structured
  data, feeds, and sitemaps accurate and consistent with visible content. Validate
  generated output and links; never invent facts or freshness signals.
