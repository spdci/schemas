# Template Profile

This folder provides a **template** for creating a country-specific or organization-specific profile of the DCI standards.

A **profile** is a localized adaptation of the base schemas. It may:

- Restrict certain fields to specific code lists or enumerations.
- Add new optional or required fields relevant to the local context.
- Remove fields that are not applicable.
- Adjust descriptions and examples for local usage.

---

## How to Create a New Profile

1. **Copy this folder** and rename it to your country or organization name, e.g.:



profiles/uganda/


2. Update the `profile-metadata.yaml` with:
- Profile name and description.
- Country, language, and version information.
- Contact details for maintainers.
- Links to relevant documentation.
- Pointer to your `schemas.yaml` file.

3. Create or update the `schemas.yaml` file to define which schema files your profile includes:
- By default, reference schemas from `common/` and `extensions/`.
- If your country/organization modifies a schema (e.g., adds a `national_id` field), copy that schema into your profile folder, make the changes, and reference the new file in `schemas.yaml`.
- This way, only changed schemas are duplicated, while the rest continue to point to the base `common/` and `extensions/`.

Example `schemas.yaml`:

    includes:
    - common/v1/person.jsonld
    - common/v1/household.jsonld
    - extensions/crvs/v1/crvsperson.jsonld
    - profiles/uganda/extensions/sr/v1/member.jsonld  # override


4. Validate your profile against the base schemas to ensure compliance.

5. Submit your profile as a **pull request** to this repository.

---

## Notes

* Profiles should **not overwrite the base schemas directly**; instead, they extend or override them via their own `schemas.yaml`.
* Each profile has its own `schemas.yaml` that acts as the authoritative list of included schemas.
* Only modified schemas should be copied into a profile directory; all unchanged files continue to reference `common/` and `extensions/`.
* Changes should be tracked in version control for transparency.

---

