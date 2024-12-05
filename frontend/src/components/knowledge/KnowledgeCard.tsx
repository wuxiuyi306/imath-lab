'use client'

import { Button } from '@/components/ui/Button'

interface KnowledgeCardProps {
  id: string
  title: string
  category: {
    main: string
    sub: string
  }
  content: {
    summary: string
  }
  metadata: {
    difficulty: number
    grade: number
    term: number
    chapter: number
  }
  onClick?: () => void
}

export function KnowledgeCard({
  title,
  category,
  content,
  metadata,
  onClick,
}: KnowledgeCardProps) {
  return (
    <div className="bg-white rounded-lg border border-gray-200 hover:shadow-lg transition-shadow p-6">
      <div className="flex justify-between items-start mb-4">
        <div>
          <h3 className="text-xl font-semibold text-gray-900 mb-2">{title}</h3>
          <div className="flex gap-2 mb-2">
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
              {category.main}
            </span>
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
              {category.sub}
            </span>
          </div>
        </div>
        <div className="flex flex-col items-end">
          <div className="flex items-center gap-1 mb-2">
            {Array.from({ length: metadata.difficulty }).map((_, i) => (
              <span key={i} className="text-yellow-400">★</span>
            ))}
            {Array.from({ length: 3 - metadata.difficulty }).map((_, i) => (
              <span key={i} className="text-gray-300">★</span>
            ))}
          </div>
          <span className="text-sm text-gray-500">
            {metadata.grade}年级 第{metadata.term}学期
          </span>
        </div>
      </div>
      
      <p className="text-gray-600 mb-4 line-clamp-2">{content.summary}</p>
      
      <div className="flex justify-between items-center">
        <span className="text-sm text-gray-500">
          第{metadata.chapter}章
        </span>
        <Button
          variant="outline"
          size="sm"
          onClick={onClick}
        >
          查看详情
        </Button>
      </div>
    </div>
  )
}
