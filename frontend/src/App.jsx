import { useState, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Rocket, 
  Archive, 
  MessageSquare, 
  Upload, 
  BrainCircuit, 
  Download,
  Save,
  ChevronDown
} from 'lucide-react';
import ReactMarkdown from 'react-markdown';

export default function App() {
  const [activeTab, setActiveTab] = useState('analysis');
  const [isStrictAnonymization, setIsStrictAnonymization] = useState(true);
  const [modelChoice, setModelChoice] = useState('Gemini Flash Lite (Active Pipeline)');

  const [jobDescFile, setJobDescFile] = useState(null);
  const [candidateEmail, setCandidateEmail] = useState('');
  const [resumeFile, setResumeFile] = useState(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [hasResult, setHasResult] = useState(false);
  const [reportData, setReportData] = useState('');

  const [messages, setMessages] = useState([
    { role: 'assistant', content: 'Hello! I am your HR Strategic Assistant. How can I help you regarding the current candidate?' }
  ]);
  const [chatInput, setChatInput] = useState('');

  const fileInputRef = useRef(null);
  const jdFileInputRef = useRef(null);

  const handleProcess = async () => {
    if (!jobDescFile || !resumeFile) return alert("Please provide both a Job Description file and a Resume");
    setIsProcessing(true);
    
    try {
      const formData = new FormData();
      formData.append('job_desc', jobDescFile);
      formData.append('email', candidateEmail || 'candidate@example.com');
      formData.append('resume', resumeFile);

      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        body: formData,
      });
      
      const data = await response.json();
      if (data.status === 'success') {
        setReportData(data.result);
        setHasResult(true);
      } else {
        alert("Error: " + data.message);
      }
    } catch (e) {
      alert("Failed to connect to API");
    } finally {
      setIsProcessing(false);
    }
  };

  const handleSendMessage = async () => {
    if (!chatInput.trim()) return;
    const newMsg = { role: 'user', content: chatInput };
    setMessages([...messages, newMsg]);
    setChatInput('');
    
    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: chatInput, context: reportData })
      });
      const data = await response.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.response }]);
    } catch (e) {
      setMessages(prev => [...prev, { role: 'assistant', content: 'Connection error while communicating with AI.' }]);
    }
  };

  const pageVariants = {
    initial: { opacity: 0, y: 20 },
    in: { opacity: 1, y: 0 },
    out: { opacity: 0, y: -20 }
  };

  const pageTransition = {
    type: 'tween',
    ease: 'anticipate',
    duration: 0.5
  };

  return (
    <div className="app-container">
      {/* Sidebar */}
      <div className="sidebar">
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '2rem' }}>
          <BrainCircuit size={40} color="#F5D5E0" />
          <h2 style={{ margin: 0, fontSize: '1.5rem', fontFamily: 'Outfit' }}>Smart Hire</h2>
        </div>

        <nav style={{ flex: 1 }}>
          <div 
            className={`nav-item ${activeTab === 'analysis' ? 'active' : ''}`}
            onClick={() => setActiveTab('analysis')}
          >
            <Rocket size={20} />
            New Analysis
          </div>
          <div 
            className={`nav-item ${activeTab === 'vault' ? 'active' : ''}`}
            onClick={() => setActiveTab('vault')}
          >
            <Archive size={20} />
            Resume Vault
          </div>
          <div 
            className={`nav-item ${activeTab === 'assistant' ? 'active' : ''}`}
            onClick={() => setActiveTab('assistant')}
          >
            <MessageSquare size={20} />
            HR Assistant
          </div>
        </nav>

        <div style={{ marginTop: 'auto' }}>
          <hr style={{ borderColor: 'rgba(255,255,255,0.1)', margin: '1rem 0' }} />
          
          <div style={{ marginBottom: '1rem' }}>
            <label style={{ fontSize: '0.9rem', marginBottom: '0.5rem', display: 'block', opacity: 0.8 }}>Intelligence Engine</label>
            <div style={{ position: 'relative' }}>
              <select 
                className="glass-input" 
                value={modelChoice} 
                onChange={(e) => setModelChoice(e.target.value)}
                style={{ appearance: 'none', cursor: 'pointer', paddingRight: '2.5rem' }}
              >
                <option value="Gemini Flash Lite (Active Pipeline)">Gemini Flash Lite</option>
                <option value="Gemini 2.0 Flash (Restricted Quota)">Gemini 2.0 Flash</option>
                <option value="Gemini 1.5 Pro (Authwall)">Gemini 1.5 Pro</option>
              </select>
              <ChevronDown size={16} style={{ position: 'absolute', right: '1rem', top: '50%', transform: 'translateY(-50%)', pointerEvents: 'none', opacity: 0.7 }} />
            </div>
          </div>

          <div className="toggle-container">
            <span style={{ fontSize: '0.95rem' }}>Strict Anonymization</span>
            <label className="toggle-switch">
              <input 
                type="checkbox" 
                checked={isStrictAnonymization} 
                onChange={() => setIsStrictAnonymization(!isStrictAnonymization)}
              />
              <span className="slider"></span>
            </label>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="main-content">
        <header style={{ marginBottom: '3rem' }}>
          <h1 className="main-header">Smart Hire Intelligence</h1>
          <p className="subtitle">AI-Powered Recruitment Infrastructure & Bias-Free Assessment</p>
          
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1.5rem', marginTop: '2rem' }}>
            <div className="metric-card">
              <div className="metric-value">1</div>
              <div className="metric-label">Candidates Processed</div>
            </div>
            <div className="metric-card">
              <div className="metric-value">{hasResult ? 'Calculated' : '--'}</div>
              <div className="metric-label">Match Score Status</div>
            </div>
            <div className="metric-card">
              <div className="metric-value">{hasResult ? 'Analyzed' : 'Pending'}</div>
              <div className="metric-label">Hiring Difficulty</div>
            </div>
          </div>
        </header>

        <AnimatePresence mode="wait">
          <motion.div
            key={activeTab}
            initial="initial"
            animate="in"
            exit="out"
            variants={pageVariants}
            transition={pageTransition}
          >
            {activeTab === 'analysis' && (
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '2rem' }}>
                <div className="glass-card">
                  <h3 style={{ marginTop: 0, marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <Rocket size={20} /> Opportunity Profile
                  </h3>
                  <label style={{ display: 'block', marginBottom: '0.5rem', opacity: 0.9 }}>Upload Job Description</label>
                  <div 
                      onClick={() => jdFileInputRef.current.click()}
                      style={{ 
                        border: '2px dashed rgba(255,255,255,0.2)', 
                        padding: '2rem', 
                        borderRadius: '12px', 
                        textAlign: 'center',
                        background: jobDescFile ? 'rgba(102, 103, 171, 0.2)' : 'rgba(0,0,0,0.1)',
                        cursor: 'pointer',
                        transition: 'all 0.3s'
                      }}
                    >
                      <input 
                        type="file" 
                        accept=".pdf,.txt,.md" 
                        onChange={(e) => setJobDescFile(e.target.files[0])} 
                        style={{ display: 'none' }} 
                        ref={jdFileInputRef} 
                      />
                      <Upload size={32} color="#6667AB" style={{ marginBottom: '1rem' }} />
                      <div style={{ fontWeight: 600 }}>{jobDescFile ? jobDescFile.name : 'Upload Job Description'}</div>
                      <div style={{ fontSize: '0.8rem', opacity: 0.7, marginTop: '0.5rem' }}>Drag & drop or click to browse</div>
                    </div>
                </div>

                <div className="glass-card">
                  <h3 style={{ marginTop: 0, marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <Upload size={20} /> Candidate Inputs
                  </h3>
                  
                  <div style={{ marginBottom: '1.5rem' }}>
                    <label style={{ display: 'block', marginBottom: '0.5rem', opacity: 0.9 }}>Contact Address</label>
                    <input 
                      type="email" 
                      className="glass-input" 
                      placeholder="candidate@example.com"
                      value={candidateEmail}
                      onChange={(e) => setCandidateEmail(e.target.value)}
                    />
                  </div>

                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem', marginBottom: '2rem' }}>
                    <div 
                      onClick={() => fileInputRef.current.click()}
                      style={{ 
                        border: '2px dashed rgba(255,255,255,0.2)', 
                        padding: '2rem', 
                        borderRadius: '12px', 
                        textAlign: 'center',
                        background: resumeFile ? 'rgba(102, 103, 171, 0.2)' : 'rgba(0,0,0,0.1)',
                        cursor: 'pointer',
                        transition: 'all 0.3s'
                      }}
                    >
                      <input 
                        type="file" 
                        accept=".pdf" 
                        onChange={(e) => setResumeFile(e.target.files[0])} 
                        style={{ display: 'none' }} 
                        ref={fileInputRef} 
                      />
                      <Upload size={32} color="#6667AB" style={{ marginBottom: '1rem' }} />
                      <div style={{ fontWeight: 600 }}>{resumeFile ? resumeFile.name : 'Upload Resume (PDF)'}</div>
                      <div style={{ fontSize: '0.8rem', opacity: 0.7, marginTop: '0.5rem' }}>Drag & drop or click to browse</div>
                    </div>
                    <div style={{ 
                      border: '2px dashed rgba(255,255,255,0.2)', 
                      padding: '2rem', 
                      borderRadius: '12px', 
                      textAlign: 'center',
                      background: 'rgba(0,0,0,0.1)'
                    }}>
                      <Upload size={32} color="#6667AB" style={{ marginBottom: '1rem' }} />
                      <div style={{ fontWeight: 600 }}>Intro Video (Optional)</div>
                      <div style={{ fontSize: '0.8rem', opacity: 0.7, marginTop: '0.5rem' }}>Integrity checking supported</div>
                    </div>
                  </div>

                  <button 
                    className="glass-button" 
                    style={{ width: '100%', padding: '1rem', fontSize: '1.1rem' }}
                    onClick={handleProcess}
                    disabled={isProcessing}
                  >
                    {isProcessing ? (
                      <motion.div
                        animate={{ rotate: 360 }}
                        transition={{ repeat: Infinity, duration: 1, ease: 'linear' }}
                      >
                        <BrainCircuit size={24} />
                      </motion.div>
                    ) : (
                      <>
                        <BrainCircuit size={24} /> Run Intelligence Engine
                      </>
                    )}
                  </button>

                  {hasResult && !isProcessing && (
                    <motion.div 
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      style={{ marginTop: '2rem', padding: '1.5rem', background: 'rgba(0,0,0,0.2)', borderRadius: '12px', maxHeight: '400px', overflowY: 'auto' }}
                    >
                      <h4 style={{ margin: '0 0 1rem 0', color: '#ffb3c6' }}>Strategic Dossier Generated</h4>
                      <div style={{ fontSize: '0.9rem', lineHeight: 1.5, opacity: 0.9 }}>
                        <ReactMarkdown>{reportData}</ReactMarkdown>
                      </div>
                      <div style={{ display: 'flex', gap: '1rem', marginTop: '1.5rem' }}>
                        <button className="glass-button">
                          <Download size={18} /> Download Dossier
                        </button>
                        <button className="glass-button outline">
                          <Save size={18} /> Save to Vault
                        </button>
                      </div>
                    </motion.div>
                  )}
                </div>
              </div>
            )}

            {activeTab === 'vault' && (
              <div className="glass-card" style={{ minHeight: '500px' }}>
                <h3 style={{ marginTop: 0, marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <Archive size={20} /> Talent Archive
                </h3>
                <input 
                  type="text" 
                  className="glass-input" 
                  placeholder="🔍 Search vault by skills, role, or ID..."
                  style={{ marginBottom: '2rem' }}
                />
                <div style={{ textAlign: 'center', opacity: 0.5, marginTop: '4rem' }}>
                  <Archive size={48} style={{ marginBottom: '1rem' }} />
                  <p>Check FastAPI backend for Vault endpoints.</p>
                </div>
              </div>
            )}

            {activeTab === 'assistant' && (
              <div className="glass-card" style={{ height: '600px', display: 'flex', flexDirection: 'column' }}>
                <h3 style={{ marginTop: 0, marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <MessageSquare size={20} /> HR Strategic Assistant
                </h3>
                
                <div style={{ flex: 1, overflowY: 'auto', padding: '1rem', background: 'rgba(0,0,0,0.1)', borderRadius: '12px', marginBottom: '1.5rem' }}>
                  {messages.map((msg, idx) => (
                    <motion.div 
                      initial={{ opacity: 0, x: msg.role === 'user' ? 20 : -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      key={idx} 
                      className={`chat-message ${msg.role}`}
                    >
                      <div className="avatar">
                        {msg.role === 'user' ? 'U' : <BrainCircuit size={20} />}
                      </div>
                      <div className="message-content">
                        <ReactMarkdown>{msg.content}</ReactMarkdown>
                      </div>
                    </motion.div>
                  ))}
                </div>

                <div style={{ display: 'flex', gap: '1rem' }}>
                  <input 
                    type="text" 
                    className="glass-input" 
                    placeholder="Ask about candidate fit, suggest interview questions..."
                    value={chatInput}
                    onChange={(e) => setChatInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSendMessage()}
                  />
                  <button className="glass-button" onClick={handleSendMessage}>Send</button>
                </div>
              </div>
            )}
          </motion.div>
        </AnimatePresence>
      </div>
    </div>
  );
}
