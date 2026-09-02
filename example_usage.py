from client import AutonomousSlaBreachIncidentEscalatorClient

def main():
    client = AutonomousSlaBreachIncidentEscalatorClient()
    res = client.evaluate_incident_severity_and_escalate('ErrorRate5xx', 8.5, 1.0, 'PaymentGateway')
    print('SLA Breach Incident Escalator: ' + res['incident_escalation_id'] + ' (' + res['breach_severity_tier'] + ')')
    print('Magnitude: +' + str(res['current_breach_magnitude_pct']) + '% | Playbook: ' + res['automated_remediation_playbook_triggered'])
    print('War Room: ' + res['incident_war_room_portal_url'])

if __name__ == '__main__':
    main()
