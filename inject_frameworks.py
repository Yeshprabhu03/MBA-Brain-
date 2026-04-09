import os

injections = {
    "Porter's Five Forces": "## 🎯 When Would I Use This?\n\n1. **Private Equity Industry Deep-Dive**: Before screening specific companies in the HVAC sector, use Porter's to determine if the fundamental industry structure allows for margin expansion.\n2. **Corporate Strategy M&A**: If we acquire this raw materials supplier, how will it shift our 'Bargaining Power of Suppliers' rating from High to Low?\n3. **Startup Board Meeting**: We need to identify if our software has strong enough switching costs to neutralize the 'Threat of New Entrants'.\n\n",
    "SWOT Analysis": "## 🎯 When Would I Use This?\n\n1. **Annual Leadership Offsite**: Before we set our OKRs, let's map our internal Strengths/Weaknesses against the macro external Opportunities/Threats.\n2. **Competitor Teardown**: Let's run a SWOT on our biggest rival to find their vulnerabilities (Weaknesses) that align with our upcoming product launch (Opportunities).\n3. **Marketing Campaign Prep**: Is our brand equity strong enough to absorb the backlash if this edgy campaign fails?\n\n",
    "BCG Growth-Share Matrix": "## 🎯 When Would I Use This?\n\n1. **Corporate Portfolio Rebalancing**: We need to figure out which legacy hardware business (Dog) to divest to fund our new AI software division (Question Mark).\n2. **Muted Earnings Call Defense**: Investors are worried about low revenue growth in our core product; I must explain it is formally transitioning to a 'Cash Cow' strictly managed for high yield, not growth.\n3. **Resource Allocation Meeting**: Marketing needs to stop spending all our ad budget defending the low-margin 'Dogs' just because of internal politics.\n\n",
    "Ansoff Matrix": "## 🎯 When Would I Use This?\n\n1. **Growth Strategy Mandate**: The CEO demanded 20% YoY top-line growth. I will use Ansoff to lay out the four exact paths we can take: Market Penetration, Market Development, Product Development, or Diversification.\n2. **C-Suite Risk Assessment**: The Board wants us to build a completely new product for a completely new market (Diversification). I will use Ansoff to visually demonstrate why this is the highest possible risk quadrant.\n3. **Geographic Expansion Business Case**: We are taking our existing SaaS tool to Europe. This is a classic Market Development play.\n\n",
    "Blue Ocean Strategy": "## 🎯 When Would I Use This?\n\n1. **Founding a Startup**: I cannot build another identical CRM to compete with Salesforce in a bloody Red Ocean. I must find a Blue Ocean by targeting construction companies who use paper.\n2. **Product Innovation Workshop**: Instead of adding more highly-requested, expensive features, which features can we fundamentally eliminate to create a new value curve?\n3. **Pricing Negotiation**: We don't need to match their discount because our product sits in a Blue Ocean where no direct comparables exist.\n\n",
    "Business Model Canvas": "## 🎯 When Would I Use This?\n\n1. **Seed Round Pitch Deck**: Investors don't want a 50-page business plan. I will present our entire startup on a single slide using the 9 blocks of the Business Model Canvas.\n2. **Pivot Strategy Session**: Our customer acquisition cost is too high. Let's pull up the Canvas and redraw the 'Channels' and 'Customer Relationships' blocks.\n3. **Corporate Innovation Lab**: We need to map out out how our new D2C subscription box impacts the 'Key Partners' in our traditional retail supply chain.\n\n",
    "McKinsey 7S Framework": "## 🎯 When Would I Use This?\n\n1. **Post-Merger Integration**: We've synchronized the 'Structure' and 'Systems' of the two companies, but the merger is failing because the 'Style' and 'Shared Values' are deeply incompatible.\n2. **Change Management Initiative**: If we implement this new AI software (Strategy), we must simultaneously upgrade employee training (Skills) or the entire system will break.\n3. **Organizational Audit**: We are losing talent rapidly; I need a holistic diagnostic tool to see if our 'Staff' and 'Structure' are misaligned.\n\n",
    "Balanced Scorecard": "## 🎯 When Would I Use This?\n\n1. **Quarterly Business Review (QBR)**: The CEO is hyper-fixated on the Financial metrics. I will use the Balanced Scorecard to prove that our internal processes and customer learning metrics are flashing red.\n2. **Departmental Goal Setting**: Engineering needs to ensure their OKRs aren't just 'ship code fast', but also align with the 'Customer' and 'Learning' quadrants of the scorecard.\n3. **Incentive Compensation Design**: We must tie executive bonuses to all four quadrants, ensuring they don't slash R&D (destroying 'Innovation') just to pump the 'Financial' quadrant.\n\n",
    "Lean Startup": "## 🎯 When Would I Use This?\n\n1. **New Product Ideation**: We are not spending $2M to build the full app. We will build a $500 landing page (MVP) to test if anyone actually clicks 'Pre-Order'.\n2. **Corporate R&D Funding**: Instead of fully funding this 3-year hardware project, we will provide seed funding for a 6-week Build-Measure-Learn sprint.\n3. **Pivoting a Failing Division**: The market rejected our core hypothesis. We must look at the qualitative feedback and pivot our Customer Segment before we run out of runway.\n\n",
    "Jobs to Be Done": "## 🎯 When Would I Use This?\n\n1. **Copywriting / Marketing**: Stop selling the technical specifications of the mattress. We must sell the 'Job' the user is hiring it for: A completely uninterrupted night of deep sleep.\n2. **Feature Prioritization**: Does this new dashboard feature actually help the user accomplish their fundamental 'Job', or is it just engineering bloat?\n3. **Identifying Unseen Competitors**: If the Job is 'Entertain me during my commute', Netflix isn't just competing with Hulu; they are competing with Spotify, Candy Crush, and sleep.\n\n",
    "DCF Valuation": "## 🎯 When Would I Use This?\n\n1. **Investment Banking Pitch Book**: We need to present a rigorous intrinsic valuation of the target company to prove to the board that $50/share is a fair takeover premium.\n2. **Internal Project Finance**: Should we build a new $500M factory? I will run a DCF on the projected cash flows to ensure the NPV is positive.\n3. **Value Investing Buy-Side**: The market has panicked and dumped this stock. My DCF model indicates the intrinsic value is 40% higher than the current trading price.\n\n",
    "WACC": "## 🎯 When Would I Use This?\n\n1. **Capital Allocation Decisions**: The corporate WACC is 8%. Any internal project proposing an IRR of 6% must be immediately rejected.\n2. **CFO Debt Issuance**: If we issue $1B in junk bonds, it will raise our cost of debt, fundamentally altering our WACC and destroying our equity valuation.\n3. **Divisional Performance Evaluation**: We cannot judge the Software division and the Real Estate division using the same hurdle rate; we must calculate a specific WACC for each.\n\n",
    "LBO Model": "## 🎯 When Would I Use This?\n\n1. **Private Equity Case Interview**: You have 60 minutes to build a paper LBO to determine the maximum purchase price we can pay while still hitting a 20% IRR.\n2. **Finding the Valuation Floor**: The market has crashed. What is the lowest the stock will go? I will run an LBO to see at what price private equity firms will swoop in to buy it.\n3. **Sponsor-Backed M&A Modeling**: We must determine how much debt a consortium of banks is willing to underwrite based on the target's operating cash flow.\n\n",
    "STP Framework": "## 🎯 When Would I Use This?\n\n1. **Go-To-Market Plan for a New App**: We cannot target 'everyone'. We must Segment the market by income, Target college students, and Position ourselves as the affordable luxury alternative.\n2. **Brand Repositioning**: Our legacy brand is viewed as outdated. We need to shift our Positioning statement to target a younger, hyper-online demographic.\n3. **Product Line Expansion**: If we launch a premium version of our tool, how do we Segment the user base so it doesn't cannibalize our cheap tier?\n\n",
    "MECE Principle": "## 🎯 When Would I Use This?\n\n1. **McKinsey Case Interview**: Before brainstorming randomly, I will break down 'Declining Profitability' into Revenue and Cost, ensuring my logic tree is Mutually Exclusive and Collectively Exhaustive.\n2. **Structuring a PowerPoint Presentation**: Are my three main arguments overlapping? I must ensure they are distinct (mutually exclusive) to avoid confusing the client.\n3. **Root Cause Analysis**: When investigating the supply chain failure, we must categorize the exact failure points into a MECE framework to ensure no potential variable was missed.\n\n"
}

target_files = []
for root, _, files in os.walk('/Users/yeshwanth/MBA'):
    if '.obsidian' in root or '.git' in root: continue
    for f in files:
        if f.endswith('.md'):
            basename = f[:-3]
            if basename in injections.keys() or basename.replace("-", " ") in injections.keys():
                target_files.append((os.path.join(root, f), basename))

updated_count = 0
for filepath, basename in target_files:
    matched_key = None
    for k in injections.keys():
        if k in basename or basename in k:
            matched_key = k
            break
            
    if not matched_key: continue
            
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "## 🎯 When Would I Use This?" in content: continue
        
    if "## 🔗 Connected Concepts" in content:
        split_content = content.split("## 🔗 Connected Concepts")
        new_content = split_content[0] + injections[matched_key] + "## 🔗 Connected Concepts" + split_content[1]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1

print(f"Updated {updated_count} files successfully.")
