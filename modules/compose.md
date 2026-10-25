# Compose UI

- Keep composables focused on rendering state and emitting events. Hoist state to
  the lowest owner that needs to control it; pass values and callbacks to reusable
  components instead of acquiring screen dependencies inside them.
- Keep composable bodies free of external side effects. Use effect APIs keyed to
  the values that should restart work. Dispose listeners and resources; use updated
  callback references when an effect must observe changes without restarting.
- Match state lifetime to its purpose: `remember` for composition-local values,
  saveable state for suitable recreation state, and an appropriately scoped state
  holder for screen/business work. Use lifecycle-aware collection where supported.
- Use stable item identities in lazy collections and deliberate navigation-entry
  scope for state holders. Preserve back navigation, restoration, and deep links
  when changing navigation behavior.
- Reuse theme tokens, resources, and existing components. Base layout on available
  constraints rather than device labels or assumed screen sizes; account for text
  scaling, localization, input methods, and window insets.
- Provide accessible semantics, meaningful actions, focus behavior, and adequate
  interaction targets. Verify keyboard, pointer, and touch behavior on relevant
  platforms; do not assume identical platform accessibility support.
- Keep expensive computation out of frequent recomposition. Memoize with correct
  keys when useful; use `derivedStateOf` when derived output changes less often than
  its inputs. Add caching or stability annotations only with evidence and valid contracts.
- Check state transitions and interactions, not just previews. Validate affected
  platform hosts as well as shared UI when platform behavior changes.
