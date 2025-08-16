<style>
.tab-container {
    margin-top: 20px;
}

.tab-nav {
    display: flex;
    border-bottom: 2px solid #e0e0e0;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.tab-button {
    background: none;
    border: none;
    padding: 12px 24px;
    cursor: pointer;
    font-size: 16px;
    font-weight: 500;
    color: #666;
    border-bottom: 3px solid transparent;
    transition: all 0.3s ease;
    margin-right: 10px;
    margin-bottom: 5px;
}

.tab-button:hover {
    color: #333;
    background-color: #f5f5f5;
}

.tab-button.active {
    color: #007acc;
    border-bottom-color: #007acc;
    background-color: #f8f9fa;
}

.tab-content {
    display: none;
    animation: fadeIn 0.3s ease-in;
}

.tab-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.contact-links {
    margin: 20px 0;
    text-align: center;
}

.contact-links a {
    margin: 0 10px;
    text-decoration: none;
    color: #007acc;
    font-weight: 500;
}

.contact-links a:hover {
    text-decoration: underline;
}

.research-item {
    margin-bottom: 20px;
    padding: 15px;
    border-left: 4px solid #007acc;
    background-color: #f8f9fa;
}

.research-item h4 {
    margin-top: 0;
    color: #333;
}

.publication-item {
    margin-bottom: 15px;
    padding: 12px;
    border-radius: 5px;
    background-color: #f8f9fa;
}

.publication-item strong {
    color: #007acc;
}

@media (max-width: 768px) {
    .tab-button {
        padding: 10px 16px;
        font-size: 14px;
    }
    
    .tab-nav {
        justify-content: center;
    }
}

/* Hide GitHub Pages footer elements */
.site-footer,
footer,
.footer,
.view {
    display: none !important;
}

p:contains("Hosted on GitHub Pages"),
p:contains("Theme by"),
p:contains("orderedlist") {
    display: none !important;
}
</style>



<div class="tab-container">
    <div class="tab-nav">
        <button class="tab-button active" onclick="showTab(event, 'about')">About</button>
        <button class="tab-button" onclick="showTab(event, 'research')">Research Interests</button>
        <button class="tab-button" onclick="showTab(event, 'publications')">Publications</button>
    </div>

    <div id="about" class="tab-content active">
        <h2>About Me</h2>
        
        <div class="contact-links">
            <a href="mailto:hmohanty@usc.edu">Gmail</a> ⬥ 
            <a href="https://www.linkedin.com/in/hardhik-mohanty-38862a190/" target="_blank">LinkedIn</a> ⬥ 
            <a href="https://github.com/hardhik-99" target="_blank">Github</a> ⬥ 
            <a href="https://scholar.google.com/citations?hl=en&user=99B3RkcAAAAJ&view_op=list_works&sortby=pubdate" target="_blank">Google Scholar</a>
        </div>
        
        <p>Hey sup, I am a ML researcher focusing on applications related to Blockchain and DeFi Markets at University of Southern California, Los Angeles. As you might have guessed from the location, frequent beach trips and drives along the Pacific coast are my thing. Currently, I am pursuing my PhD in Electrical and Computer Engineering along with Master's in Financial Engineering from USC (finance is like my side hustle!). It also helps build the fundamentals for my DeFi markets research.</p>
        
        <p>Prior to this, I worked as a mitacs globalink research intern at York University, Toronto. Here i explored topics like deep learning algorithms for darknet characterization and behavioral profiling of malware attacks. Overall, I had a fantastic hands-on experience with several network security projects and simultaneously improved my computational and systems skills!!</p>
        
        <p>My bachelor's and master's degree is from IIT Kharagpur, India. I majored in Electrical Engineering with a specialisation in ML, AI and its applications. I somehow (barely!) made it through the core circuity stuff but EE helped build my engineering mathematical foundation. I graduated with a 9.01 cgpa (phew!) out of 10 and department rank-2. During my undergrad research days, I explored reinforcement learning and bandit algorithms in non-stationary environment. Plus I peeked in the world of federated learning through my bachelor's thesis. Probably the reason I looked further into distributed computing and got hooked to blockchain. Also now integrating DeFi to my expertise!! (blame my try-out-new-things to stay happy mindset)</p>
        
        <p>I am a budding expert in my research field constantly gaining delta knowledge everyday. Also, creating new niche areas for fellow researchers to get baffled on. Look at the other tabs for more details on my interests and work! I love collaborations and networking with people academically!! Do reach out through my contacts for a discussion.</p>
    </div>

    <div id="research" class="tab-content">
        <h2>Research Interests</h2>
        <p>My current research looks into the following aspects of blockchain and cryptocurrency:</p>
        
        <div class="research-item">
            <h4>Machine Learning for Cryptocurrency</h4>
            <p>Investigating robust AI methods for cryptocurrency markets to optimize trading strategies, detect fraud, and predict market trends. Applying ensemble learning techniques, GNNs, and other AI/ML models to handle noisy, imperfect, and dynamic data streams. Exploring applications of ML in improving blockchain scalability, stability, and security.</p>
        </div>
        
        <div class="research-item">
            <h4>Tokenomics and Incentive Design</h4>
            <p>Analyzing the economic models underlying blockchain-based tokens plus focusing on incentive structures, governance mechanisms, and network effects. This includes designing token distribution schemes and studying their impact on user behavior and network sustainability.</p>
        </div>
        
        <div class="research-item">
            <h4>Consensus in Dynamic Networks</h4>
            <p>Focusing on the development of consensus mechanisms tailored for dynamic and heterogeneous blockchain environments. Researching protocols like HotStuff and Tendermint that can adjust to network changes and ensure robustness. Developing consensus algorithms that maintain consistency and recover efficiently from network partitions inspired by recent advancements in the Avalanche protocol.</p>
        </div>
        
        <div class="research-item">
            <h4>Micropayments in Decentralized Networks</h4>
            <p>Enhancing the efficiency and security of micropayments for frequent, low-value transactions. Implementing schemes like probabilistic payment channels that reduce transaction overhead while ensuring security. Improving the scalability and reliability of off-chain solutions such as the Lightning Network for Bitcoin and Raiden Network for Ethereum.</p>
        </div>
    </div>

    <div id="publications" class="tab-content">
        <h2>Publications</h2>
        
        <div class="publication-item">
            <strong>1.</strong> <strong>Hardhik Mohanty</strong>, Giovanni Zaarour, and Bhaskar Krishnamachari. "Proactive Market Making and Liquidity Analysis for Everlasting Options in DeFi Ecosystems." <em>arXiv preprint</em> arXiv:2508.07068 (2025).
        </div>
        
        <div class="publication-item">
            <strong>2.</strong> Moein Shafi, Arash Habibi Lashkari, and <strong>Hardhik Mohanty</strong>. "Unveiling malicious DNS behavior profiling and generating benchmark dataset through application layer traffic analysis." <em>Computers and Electrical Engineering</em> 118 (2024): 109436.
        </div>
        
        <div class="publication-item">
            <strong>3.</strong> Ryan Lavin, Xuekai Liu, <strong>Hardhik Mohanty</strong>, Logan Norman, Giovanni Zaarour, and Bhaskar Krishnamachari. "A Survey on the Applications of Zero-Knowledge Proofs." <em>arXiv preprint</em> arXiv:2408.00243 (2024).
        </div>
        
        <div class="publication-item">
            <strong>4.</strong> Gaines Odom, <strong>Hardhik Mohanty</strong>, Ujjwal Guin, and Bhaskar Krishnamachari. "Blockchain-Enabled Whitelisting Mechanisms for Enhancing Security in 3D ICs." <em>Proceedings of the Great Lakes Symposium on VLSI</em> (2024): 483-488.
        </div>
        
        <div class="publication-item">
            <strong>5.</strong> Zhenbang Feng, <strong>Hardhik Mohanty</strong>, and Bhaskar Krishnamachari. "Modeling and Analysis of Crypto-Backed Over-Collateralized Stable Derivatives in DeFi." <em>Frontiers in Blockchain</em> 7 (2024): 1392812.
        </div>
        
        <div class="publication-item">
            <strong>6.</strong> <strong>Hardhik Mohanty</strong>, Arousha Haghighian Roudsari, and Arash Habibi Lashkari. "Robust stacking ensemble model for darknet traffic classification under adversarial settings." <em>Computers & Security</em> 120 (2022): 102830.
        </div>
        
        <div class="publication-item">
            <strong>7.</strong> Gourab Ghatak, <strong>Hardhik Mohanty</strong>, and Aniq Ur Rahman. "Kolmogorov-Smirnov test-based actively-adaptive Thompson sampling for non-stationary bandits." <em>IEEE Transactions on Artificial Intelligence</em> 3.1 (2021): 11-19.
        </div>
        
        <p style="margin-top: 20px; font-style: italic; text-align: center;">Hopefully a lot more to come, stay tuned ;)</p>
    </div>
</div>

<script>
function showTab(evt, tabName) {
    var i, tabcontent, tablinks;
    
    // Hide all tab content
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].classList.remove("active");
    }
    
    // Remove active class from all tab buttons
    tablinks = document.getElementsByClassName("tab-button");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
    }
    
    // Show the selected tab and mark button as active
    document.getElementById(tabName).classList.add("active");
    evt.currentTarget.classList.add("active");
}

// Ensure the About tab is shown by default when page loads
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('about').classList.add('active');
    document.querySelector('.tab-button').classList.add('active');
});
</script>
