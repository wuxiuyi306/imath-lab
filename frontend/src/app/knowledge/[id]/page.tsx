// 模拟数据，实际应该从API获取
const mockKnowledgePoint = {
  id: '1',
  title: '一元二次方程',
  category: {
    main: '代数',
    sub: '方程'
  },
  content: {
    summary: '一元二次方程是一种基本的代数方程，形如ax²+bx+c=0（其中a≠0）。它在数学中有广泛的应用，是初中代数的重要内容之一。',
    keyPoints: [
      '一元二次方程的标准形式：ax²+bx+c=0（a≠0）',
      '求解方法：配方法、因式分解法、公式法',
      '判别式Δ=b²-4ac的作用和意义',
      '韦达定理及其应用'
    ],
    explanation: `一元二次方程是数学中一个重要的概念，它是研究二次函数的基础。
    解一元二次方程的方法主要有：
    1. 因式分解法：适用于容易分解的情况
    2. 配方法：通过配方转化为完全平方式
    3. 公式法：利用求根公式x=(-b±√(b²-4ac))/(2a)
    
    解题时应根据具体情况选择合适的方法。`,
    examples: [
      {
        title: '例1：解方程x²+2x+1=0',
        content: '解：这是一个可以因式分解的方程\n(x+1)²=0\n解得：x=-1（重根）'
      },
      {
        title: '例2：解方程x²-4x+3=0',
        content: '解：使用因式分解法\nx²-4x+3=(x-1)(x-3)\n解得：x=1或x=3'
      }
    ]
  }
}

export default function KnowledgeDetailPage({ params }: { params: { id: string } }) {
  return (
    <div className="container py-8">
      <div className="max-w-4xl mx-auto">
        {/* 头部信息 */}
        <div className="mb-8">
          <div className="flex items-start mb-4">
            <div>
              <h1 className="text-3xl font-bold text-gray-900 mb-2">{mockKnowledgePoint.title}</h1>
              <div className="flex gap-2">
                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                  {mockKnowledgePoint.category.main}
                </span>
                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
                  {mockKnowledgePoint.category.sub}
                </span>
              </div>
            </div>
          </div>
          
          <p className="text-gray-600">{mockKnowledgePoint.content.summary}</p>
        </div>

        {/* 知识要点 */}
        <div className="mb-8">
          <h2 className="text-2xl font-semibold text-gray-900 mb-4">知识要点</h2>
          <ul className="list-disc list-inside space-y-2">
            {mockKnowledgePoint.content.keyPoints.map((point, index) => (
              <li key={index} className="text-gray-700">{point}</li>
            ))}
          </ul>
        </div>

        {/* 详细解释 */}
        <div className="mb-8">
          <h2 className="text-2xl font-semibold text-gray-900 mb-4">详细解释</h2>
          <div className="prose max-w-none">
            {mockKnowledgePoint.content.explanation.split('\n').map((paragraph, index) => (
              <p key={index} className="mb-4 text-gray-700">{paragraph.trim()}</p>
            ))}
          </div>
        </div>

        {/* 例题 */}
        <div className="mb-8">
          <h2 className="text-2xl font-semibold text-gray-900 mb-4">例题</h2>
          <div className="space-y-6">
            {mockKnowledgePoint.content.examples.map((example, index) => (
              <div key={index} className="bg-gray-50 rounded-lg p-6">
                <h3 className="font-semibold text-gray-900 mb-2">{example.title}</h3>
                <pre className="whitespace-pre-wrap text-gray-700">{example.content}</pre>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
