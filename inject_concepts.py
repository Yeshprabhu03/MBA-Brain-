import os

replacements = {
    "Netflix Disruption Case": """## 🔗 Connected Concepts

- [[Disruptive Innovation]]: The classic framework explaining how streaming replaced DVDs.
- [[Value Chain Analysis]]: Netflix eliminated physical distribution and stores from the value chain.
- [[Porter's Five Forces]]: Shows the intense competition Netflix now faces in the 'Streaming Wars'.
- [[First Principles Thinking]]: Hastings realized entertainment relies on data delivery, not physical discs.
- [[Core Competencies]]: Netflix's shift from logistics to content creation algorithms.
- [[Business Model Canvas]]: The shift from pay-per-rental to subscription recurring revenue.
- [[Economies of Scale]]: Why Netflix's massive user base allows them to outspend rivals on original content.
- [[Network Effects]]: The data-flywheel where more viewers provide better algorithmic recommendations.

""",
    "WeWork Rise and Fall": """## 🔗 Connected Concepts

- [[Corporate Governance]]: The catastrophic failure of the Board of Directors to check Adam Neumann.
- [[Agency Theory]]: Extreme misalignment between regular shareholders and the CEO's self-dealing.
- [[VRIO Framework]]: Real estate arbitrage is easily imitable, meaning they had no sustained moat.
- [[Business Model Canvas]]: Evaluates the fatal flaw of borrowing short-term to lend long-term.
- [[Organizational Culture]]: A toxic, cult-like internal environment masking financial insolvency.
- [[Cost of Capital]]: Neumann's growth was fueled by zero-interest-rate environment funds.
- [[Network Effects]]: WeWork falsely claimed physical office space possessed strong digital networking moats.
- [[Ethics & ESG MOC]]: Flagrant disregard for financial transparency and ethical corporate behavior.

""",
    "Kodak Digital Failure": """## 🔗 Connected Concepts

- [[Disruptive Innovation]]: The textbook example of a company inventing the disruption but suppressing it.
- [[The Innovator's Dilemma]]: Why protecting the high-margin film business destroyed the overall company.
- [[Core Rigidities]]: When former strengths (chemical engineering) become weaknesses in a digital era.
- [[Organizational Culture]]: A culture dominated by chemists rather than forward-thinking technologists.
- [[BCG Growth-Share Matrix]]: Kodak treated digital as a 'Dog' instead of a 'Question Mark'.
- [[Scenario Planning]]: The strategic failure to accurately forecast the exponential curve of sensor tech.
- [[Value Proposition]]: Consumers wanted to share memories, not necessarily print physical photos.
- [[First Principles Thinking]]: Failing to understand the fundamental job was visual capture, not film.

""",
    "BlackBerry Decline": """## 🔗 Connected Concepts

- [[Disruptive Innovation]]: Apple shifted the phone from a productivity tool to a consumer entertainment platform.
- [[The Innovator's Dilemma]]: BlackBerry ignored touchscreens to protect their keyboard-loving enterprise customer base.
- [[Platform Strategy]]: Apple opened the App Store; BlackBerry kept a closed ecosystem and lost the developer war.
- [[Network Effects]]: The iOS developer ecosystem created an uncopyable, cross-sided network moat.
- [[User Experience (UX)]]: The paradigm shift from physical tactile feedback to software flexibility.
- [[Value Chain Analysis]]: Moving value from hardware (keyboards) to localized software integrations.
- [[Competitive Advantage]]: How a previously dominant moat vaporizes during an industry paradigm shift.
- [[Jobs to Be Done]]: Realizing smartphones were hired for internet browsing, not just secure email.

""",
    "Southwest Airlines Strategy": """## 🔗 Connected Concepts

- [[Porter's Generic Strategies]]: A flawless execution of the 'Cost Leadership' quadrant.
- [[Operations Strategy]]: Point-to-point routing vs. the traditional hub-and-spoke legacy model.
- [[Lean Manufacturing]]: Treating plane turnaround times with the same urgency as single-minute exchange of dies.
- [[Organizational Culture]]: A deeply ingrained employee-first culture driving exceptional customer service.
- [[Core Competencies]]: Utilizing a single aircraft type (Boeing 737) to drastically slash maintenance training.
- [[Value Chain Analysis]]: Eliminating travel agents, meals, and assigned seating to lower the cost floor.
- [[Blue Ocean Strategy]]: Initially competing against buses and cars, not other airlines.
- [[Continuous Improvement (Kaizen)]]: The relentless drive to optimize boarding and deplaning metrics.

""",
    "Starbucks Delivering Customer Service": """## 🔗 Connected Concepts

- [[Value Proposition]]: Shifting from selling coffee to selling the "Third Place" between work and home.
- [[Customer Lifetime Value]]: Realizing that a high-retention customer justifies massive upfront satisfaction costs.
- [[Service Profit Chain]]: The direct mathematical link between employee satisfaction and customer loyalty.
- [[Organizational Behavior]]: How Howard Schultz created a culture of empowerment for baristas.
- [[Brand Equity]]: Building a premium lifestyle brand that allows for massive pricing power over commodity coffee.
- [[Operations Strategy]]: The tension between increasing speed of service and maintaining hand-crafted quality.
- [[Lean Startup]]: Rapidly testing customer reactions to automated espresso machines vs manual pulls.
- [[Process Mapping]]: Reducing physical barista movements to shave seconds off the drivethrough times.

""",
    "Walmart Supply Chain Innovation": """## 🔗 Connected Concepts

- [[Supply Chain Management]]: Walmart set the global standard for cross-docking and inventory velocity.
- [[Cost Leadership]]: Using extreme supply chain efficiencies to pass savings to the consumer and undercut rivals.
- [[Porter's Five Forces]]: Achieving massive bargaining power over suppliers due to unprecedented retail scale.
- [[Operations Strategy]]: The implementation of RFID and satellite communications long before competitors.
- [[Economies of Scale]]: Why a Mom-and-Pop competitor cannot mathematically match their localized cost structure.
- [[VRIO Framework]]: Their proprietary logistics software (Retail Link) became a rare and inimitable resource.
- [[Inventory Turnover]]: Maintaining massive ROIC despite low net margins by flipping inventory rapidly.
- [[First Principles Thinking]]: Rethinking retail distribution from direct-to-store to centralized, automated hubs.

""",
    "Google Project Aristotle": """## 🔗 Connected Concepts

- [[Psychological Safety]]: The number one proven determinant of high-performing teams, overshadowing raw IQ.
- [[Organizational Behavior]]: How team dynamics and unwritten rules dictate overall corporate output.
- [[Leadership Styles]]: Why leaders who display vulnerability build significantly stronger teams.
- [[Team Effectiveness]]: Proving that "who" is on a team matters far less than "how" the team interacts.
- [[Corporate Culture]]: The intentional engineering of environments where risk-taking is celebrated.
- [[Data-Driven Decision Making]]: Applying strict analytical rigor to traditionally "soft" HR topics.
- [[OKR Framework]]: How psychologically safe teams are empowered to set wildly ambitious goals.
- [[Continuous Improvement (Kaizen)]]: Feedback loops only function when employees aren't afraid of retaliation.

""",
    "Enron Culture Collapse": """## 🔗 Connected Concepts

- [[Organizational Culture]]: How the hyper-competitive "Rank and Yank" system obliterated moral boundaries.
- [[Corporate Governance]]: The catastrophic failure of the Board to police the CFO's blatant conflicts of interest.
- [[Agency Theory]]: Executives looted the company for personal gain, destroying the principals' (shareholders) equity.
- [[Ethics & ESG MOC]]: The defining modern case study in business ethics and the necessity of whistleblowers.
- [[Psychological Safety]]: A completely toxic environment where questioning the leadership resulted in termination.
- [[Financial Statement Analysis]]: The failure of Wall Street to correctly interpret off-balance-sheet debt.
- [[Incentive Design]]: Why paying bonuses strictly based on mark-to-market revenue estimates guarantees logical fraud.
- [[Leadership Styles]]: Skilling and Lay's arrogant, opaque leadership directly fostered systemic criminality.

"""
}

def update_file(filename, replacement_text):
    for root, _, files in os.walk('/Users/yeshwanth/MBA'):
        if filename + '.md' in files:
            path = os.path.join(root, filename + '.md')
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple replacement logic: find "## 🔗 Connected Concepts", split, keep the footer if it exists.
            if "## 🔗 Connected Concepts" in content:
                parts = content.split("## 🔗 Connected Concepts")
                top = parts[0]
                bottom = parts[1]
                
                # Try to preserve the footer. Usually starts with *← or --- loosely at bottom
                footer = ""
                if "*←" in bottom:
                    footer_idx = bottom.rfind("*←")
                    footer = "\n\n" + bottom[footer_idx:]
                elif "---" in bottom and len(bottom) - bottom.rfind("---") < 100:
                    footer_idx = bottom.rfind("---")
                    footer = "\n\n" + bottom[footer_idx:]
                    
                new_content = top + replacement_text + footer
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            return

for k, v in replacements.items():
    update_file(k, v)

