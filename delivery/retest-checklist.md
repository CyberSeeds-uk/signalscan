# Retest Checklist

Use this checklist when conducting a retest after the client has implemented recommendations from the initial SignalScan report.

1. **Confirm Scope**
   - [ ] Review which findings have been addressed and which are still outstanding.
   - [ ] Confirm any new domains or assets to include in the retest.

2. **Update Configuration**
   - [ ] Modify the YAML config file with any new domains or settings.
   - [ ] Run `validate_engagement.py` to ensure validity.

3. **Repeat Passive Checks**
   - [ ] Run `signalscan_collect.py` for the primary and related domains.
   - [ ] Focus on findings marked for retest; collect evidence demonstrating improvements or persisting issues.

4. **Compare Findings**
   - [ ] Compare new observations against previous evidence.
   - [ ] Note changes in trust/security impact, commercial impact, urgency and ease of repair.

5. **Update Report**
   - [ ] Update the findings JSON with new statuses (e.g. “verified – resolved”, “verified – unresolved”).
   - [ ] Generate an updated report highlighting improvements and remaining gaps.

6. **Next Steps**
   - [ ] Recommend any new actions based on the retest.
   - [ ] Discuss with the client whether ongoing monitoring (SignalWatch) is appropriate.

7. **Evidence Management**
   - [ ] Save new evidence in the `04-retest` folder of the client’s directory.
   - [ ] Update the data retention schedule accordingly.

Following this checklist helps ensure retests are methodical, measurable and aligned with the client’s objectives.