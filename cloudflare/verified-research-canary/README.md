# Verified Research Alert Delivery Canary

This Worker is the recipient-side witness for GlassesResearch alert delivery. It is not a subscriber mailbox and it does not retain message bodies.

Production address: `delivery@canary.glassesresearch.org`

The Worker accepts only signed synthetic messages created by the Verified Research Alerts Worker. A valid receipt writes the publication ID, receive timestamp, and Message-ID (when present) into the shared D1 database. The publisher then queries the authenticated `/delivery-proof` endpoint on the alerts Worker and fails unless that receipt exists.

See `../verified-research-alerts/CANARY_DESIGN.md` for the complete delivery contract.
